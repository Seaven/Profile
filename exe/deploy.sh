
function run() {
    for i in `seq $#`; do
        if [[ $1 == 'fe' ]]; then
            echo "stop fe"
            
            ./fe/bin/stop_fe.sh
            sleep 1
            rm -rf ./fe/lib
            cp -r  ${DORIS}/output/fe/lib ~/doris/fe/lib
            
	    rm -rf ./fe/log/*
            ./fe/bin/start_fe.sh --daemon
            
            echo "start fe finish"
        else           
            echo "stop $1"

            ./$1/bin/stop_be.sh
            sleep 1
            cp ${DORIS}/output/be/lib/palo_be ~/doris/$1/lib/
            rm -f ~/doris/$1/log/*
            ./$1/bin/start_be.sh --daemon
    
            echo "start $1 finish"
        fi
   
        shift
    done
}



if [[ $1 == 'all' ]]; then
    echo "restart & delay all"
    run fe be1 be2 be3
else 
    run $@
fi
