#!/bin/bash

LOG_FILE="./LOGFILE.txt"

lastline=$( tail -n 1 LOGFILE.txt )
firstword=$(echo $lastline | cut -d " " -f1)


if [[ $# -eq 0 ]] ; then
  echo "No arguments given. Commands: Start, end, status, log'"

elif [[ $# -eq 1 ]] ; then

  if [[ "$1" == "start" ]] ; then
    echo "error, start takes 2 arguments"

  elif [[ "$1" == "stop" ]] ; then

    if [[ "$firstword" == "LABEL" ]] ; then
      echo END $(date) >> $LOG_FILE

    else
      echo "error! no task running"
    fi

  elif [[ "$1" == "status" ]] ; then

    if [[ "$firstword" == "LABEL" ]] ; then
      taskname=$(echo $lastline | cut -d " " -f2-)
      echo "current task: $taskname"

    else
      echo "error! no task running"
    fi

  elif [[ "$1" == "log" ]] ; then
    while read line
      do
        mode=$(echo "$line" | cut -d " " -f1)

        if [[ $mode == "START" ]] ; then
          start=$(echo "$line" | cut -d " " -f5)

        elif [[ $mode == "LABEL" ]] ; then
          label=$(echo "$line" | cut -d " " -f2-)

        elif [[ $mode == "END" ]] ; then
          end=$(echo "$line" | cut -d " " -f5)
          start_time=$(date +%s -d $start)
          end_time=$(date +%s -d $end)
          secs="$(($end_time - $start_time))"
          hh_mm_ss=$(date -ud "@$secs" +"%H:%M:%S")


          echo "$label": $hh_mm_ss
        fi
      done < $LOG_FILE
  fi

elif [[ $# -eq 2 ]] ; then
  if [[ "$1" == "start" ]] ; then
    if [[ $firstword == 'LABEL' ]] ; then
      echo "error, task in progress"
    elif [[ $firstword == 'END' ]] ; then
      echo START $(date) >> $LOG_FILE
      echo LABEL $2 >> $LOG_FILE
    fi
  else
    echo "$1 only takes 1 argument"
  fi
else
  echo "Too many arguments given"

fi
