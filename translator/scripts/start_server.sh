#!/bin/bash
rm -rf logs
mkdir logs

nohup python server/master_api.py > logs/master_api.out 2>&1 &
nohup python server/rq_worker_sts.py > logs/sts.out 2>&1 &
nohup python server/rq_worker_stt.py > logs/stt.out 2>&1 &
nohup python server/rq_worker_tts.py > logs/tts.out 2>&1 &
nohup python server/rq_worker_ttt.py > logs/ttt.out 2>&1 &