
function stop() {
    for i in `seq $#`; do
        echo "stop $1"
        ./$1/bin/stop_*.sh
        echo "stop $1 finish"
        shift
    done
}

if [[ $# == 1 && $1 == 'all' ]]; then
    echo 'stop all'
    stop fe be1 be2 be3
else
    echo "stop $@"
    stop $@
fi
