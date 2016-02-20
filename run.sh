#!/bin/bash

show_help() { 
        echo -e "\nUsage:\n$0 -c {tag|search} -d {/path/to/directory}  \n" 
}
 

if [ $# -lt 1 ]; then
   show_help
   exit 1
fi

OPTIND=1         # Reset in case getopts has been used previously in the shell.

directory_path=""

while getopts "h?:c:d:" opt; do
    case "$opt" in
    h|\?)
        show_help
        exit 0
        ;;
    c)  command_name=$OPTARG
        if [ "$OPTARG" == "tag" ] 
        then
            tag=1

        elif [ "$OPTARG" == "search" ]
        then
            tag=0
        else
            echo "Invalid command"
            show_help
            exit 1
        fi
        ;;
    d)  directory_path=$OPTARG
        ;;
    esac
done

shift $((OPTIND-1))

[ "$1" = "--" ] && shift

if [ $tag -eq 1 ]
then
    if [ -z "$directory_path" ]
    then
       echo "Please specify directory path"
       show_help
       exit 1
    fi 
    python tag.py $directory_path
else
    python search.py 
fi

