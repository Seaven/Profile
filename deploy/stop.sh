
function stop() {
    for i in `seq $#`; do
        echo "stop $1"
        if [[ $1 == 'fe' ]]; then
            ./$1/bin/stop_fe.sh
        else 
            ./$1/bin/stop_be.sh
        fi
        echo "stop $1 finish"
        shift
    done
}

if [[ $# == 1 && $1 == 'all' ]]; then
    echo 'stop all'
    stop fe be1 be2 be3
elif [[ $# == 1 && $1 == 'be' ]]; then
    echo 'stop be'
    stop be1 be2 be3
elif [[ $# == 1 && $1 == 'broker' ]]; then
    echo 'stop broker'
    stop broker
else
    echo "stop $@"
    stop $@
fi
