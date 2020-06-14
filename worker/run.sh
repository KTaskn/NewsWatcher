
download_date=`date +%Y%m%d%H%M%S`

while read row; do
    echo $row
    shinbun=`echo ${row} | cut -d , -f 1`
    url=`echo ${row} | cut -d , -f 2`
    /work/download.sh $download_date $shinbun $url
done < /work/urls.csv
