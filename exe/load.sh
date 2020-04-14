DA=`date "+%Y%m%d%H%M%S"`
LABEL=`echo ${1}_${DA}`
curl --location-trusted -u root -T ${1} http://localhost:8090/api/test/${1}/_load?label=${LABEL}



