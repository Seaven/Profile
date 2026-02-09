function run() {
	for i in $(seq $#); do
		if [[ $1 == 'fe' ]]; then
			echo "stop fe"

			./fe/bin/stop_fe.sh
			sleep 1
			rm -rf ./fe/lib
			cp -r ${SR}/output/fe/lib fe/lib

			rm -rf ./fe/log/*
			./fe/bin/start_fe.sh --daemon

			echo "start fe finish"
		else
			echo "stop $1"

			./$1/bin/stop_be.sh
			sleep 1
			cp -r ${SR}/output/be/lib/starrocks_be* ~/doris/$1/lib/
			rm -f ~/doris/$1/log/*
			./$1/bin/start_be.sh --daemon

			echo "start $1 finish"
		fi

		shift
	done
}

if [[ $1 == 'sr' ]]; then
	SR=$HOME/workspace/StarRocks
	shift
elif [[ $1 == 'dr' ]]; then
	SR=${DR}
	shift
fi
echo "source from ${SR}"

if [[ $1 == 'all' ]]; then
	echo "restart & deploy all"
	run fe be1 be2 be3
elif [[ $1 == 'be' ]]; then
	echo "restart & deploy all be"
	run be1 be2 be3
elif [[ $1 == 'broker' ]]; then
	echo "restart & deploy broker"
	sh ./broker/bin/stop_broker.sh
	rm -rf ./broker/lib
	cp -r ${SR}/fs_brokers/apache_hdfs_broker/output/apache_hdfs_broker/lib broker/lib

	rm -f ./broker/log/*

	sh ./broker/bin/start_broker.sh --daemon
	echo "start broker finish"
else
	run $@
fi
