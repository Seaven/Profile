function start() {
    for i in `seq $#`; do
        echo "start $1"
        if [[ $1 == 'fe' ]]; then
            ./$1/bin/start_fe.sh --daemon
        else 
            ./$1/bin/start_be.sh --daemon
        fi
        echo "start $1 finish"
        shift
    done
}

if [[ $# == 1 && $1 == 'all' ]]; then
    echo 'start all'
    start fe be1 be2 be3
elif [[ $# == 1 && $1 == 'be' ]]; then
    echo 'start be'
    start be1 be2 be3
elif [[ $# == 1 && $1 == 'broker' ]]; then
    echo 'start broker'
    start broker
else
    echo "start $@"
    start $@
fi
