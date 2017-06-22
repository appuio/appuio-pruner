#!/usr/bin/python

import os
import subprocess
import json
from StringIO import StringIO

class JobsCleaner:
  def __init__(self, keep_number_of_jobs):
    if not isinstance(keep_number_of_jobs, int):
      raise TypeError("keep_number_of_jobs must be an integer")
    self.keep_number_of_jobs = keep_number_of_jobs

    p = subprocess.Popen(['oc', 'project', 'default'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, err) = p.communicate()

    if err:
      print err


  def filter_newest_jobs(self, jobs_dict):
    for i in range(self.keep_number_of_jobs):
      max_val = max(jobs_dict.values())
      max_val_key = [key for key, val in jobs_dict.iteritems() if val == max_val]
      del jobs_dict[str(max_val_key[0])]

    return jobs_dict


  def delete_jobs(self, jobs_dict, project):
    for job_name in jobs_dict.iterkeys():
      p = subprocess.Popen(['oc', 'delete', 'job', str(job_name), '-n', project], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      (output, err) = p.communicate()

      if err:
        print err
      else:
        print output


  # wrapper method
  def clean_jobs(self):
    # get all scheduledJobs
    p = subprocess.Popen(['oc', 'get', '--all-namespaces', 'scheduledjob', '-o', 'json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, err) = p.communicate()
    scheduled_jobs = json.load(StringIO(output))

    # get all jobs
    p = subprocess.Popen(['oc', 'get', '--all-namespaces', 'job', '-o', 'json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, err) = p.communicate()
    jobs = json.load(StringIO(output))
    
    for sj in scheduled_jobs['items']:
      scheduled_job_name = sj['metadata']['name']
      scheduled_job_project = sj['metadata']['namespace']

      succeeded_jobs = dict()
      failed_jobs = dict()

      for j in jobs['items']:
        if scheduled_job_project in j['metadata']['namespace']:
          if "\"" + scheduled_job_name + "\"" in j['metadata']['annotations']['kubernetes.io/created-by'] and "completionTime" in j['status']:
            job_name = j['metadata']['name']
            job_completion_time = j['status']['completionTime']
            job_succeeded = j['status']['succeeded']
    
            if job_succeeded == 1:
              succeeded_jobs[job_name] = job_completion_time
            else:
              failed_jobs[job_name] = job_completion_time

      if len(succeeded_jobs) > self.keep_number_of_jobs:
        succeeded_jobs_filtered = self.filter_newest_jobs(succeeded_jobs)
        self.delete_jobs(succeeded_jobs_filtered, scheduled_job_project)

      if len(failed_jobs) > self.keep_number_of_jobs:
        failed_jobs_filtered = self.filter_newest_jobs(failed_jobs)
        self.delete_jobs(failed_jobs_filtered, scheduled_job_project)


def main():
  cleaner = JobsCleaner(int(os.getenv('JOBS_NUMBER_TO_KEEP', '3')))
  cleaner.clean_jobs()


if __name__ == "__main__": main()

