DIRNAME_ARCHIVES=/archives
download_date=$1
shinbun=$2
url=$3

name=${download_date}_${shinbun}
savedir=${DIRNAME_ARCHIVES}/${name}
mkdir savedir

echo ${savedir}
wget -P ${savedir} -A .html ${url}