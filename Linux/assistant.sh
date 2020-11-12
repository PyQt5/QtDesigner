#!/bin/sh

basedir=`dirname $0`
basedir=`cd $basedir;pwd`

cd -P ${basedir}

#export QT_DEBUG_PLUGINS=1
export LD_LIBRARY_PATH=${basedir}/lib:$LD_LIBRARY_PATH

chmod +x ${basedir}/bin/assistant
${basedir}/bin/assistant $@ &
