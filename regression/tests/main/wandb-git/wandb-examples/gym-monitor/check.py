#!/usr/bin/env python

# Common code (refactor into regression framework at some point)
import os
import wandb
run_id = os.environ.get("WANDB_RUN_ID")
project = os.environ.get("WANDB_PROJECT") or "regression"
api = wandb.Api()
last_run = api.run("%s/%s" % (project, run_id))

#
# Test Checks
#
assert last_run, "can not find run"
assert last_run.state == "finished"
assert last_run.project == project

#
# Test Checks
#
video = last_run.summary_metrics["videos"]
assert video.get("_type") == "video-file"
assert video.get("size") > 0
file_names = set([f.name for f in last_run.files()])
assert video.get("path") in file_names
