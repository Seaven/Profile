
function start() {
    for i in `seq $#`; do
        echo "start $1"
        ./$1/bin/start_*.sh --daemon
        
        echo "start $1 finish"
        shift
    done
}


if [[ $# == 1 && $1 == 'all' ]]; then
    echo 'start all'
    start fe be1 be2 be3
else
    echo "start $@"
    start $@
fi
