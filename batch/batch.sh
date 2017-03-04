#!/usr/bash

function usage() {
    echo "to execute command in machine which you want"
    echo "usage:"
    echo "     sh bash.sh username host_list_file password command"
    return 0
}


function main() {
    
    if [[ $# -lt 4 ]];then   
        usage
        return 0
    fi
    
    local user=$1
    shift
    local file=$1
    shift
    local password=$1
    shift
    local command=$(echo $@)
    
    echo $command

    for line in $(cat $file); do
        {
            ./batch.exp $user $line $password "$command"
        } &
    done
    
}

main $@
