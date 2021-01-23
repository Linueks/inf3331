#!/bin/bash

if [[ $# -eq 0 ]] ; then
  echo "No argument given, defaulting to 1"
  cd ..
elif [[ $#=>1 ]] ; then
  for ((i=1; i<=$#; i++))
    do
      cd ..
    done
fi
