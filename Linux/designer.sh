#!/bin/sh

basedir=`dirname $0`
basedir=`cd $basedir;pwd`

cd -P ${basedir}

export LD_LIBRARY_PATH=${basedir}/lib

${basedir}/bin/designer $@
