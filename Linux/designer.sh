#!/bin/sh

basedir=`dirname $0`
basedir=`cd $basedir;pwd`

cd -P ${basedir}

#export QT_DEBUG_PLUGINS=1
export PYTHONHOME=${basedir}
export PYTHONPATH=${basedir}/local/lib/python3.6/:${basedir}/local/lib/python3.6/lib-dynload/:${basedir}/local/lib/python3.6/site-packages/:${basedir}/local/lib64/python3.6/site-packages/
export LD_LIBRARY_PATH=${basedir}/local/lib64:${basedir}/lib

chmod -R +x ${basedir}/bin/*
${basedir}/bin/designer $@ &
