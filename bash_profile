# .bash_profile

# Get the aliases and functions
PS1='\[\033[00m\]\u\[\033[00m\]@\h:\[\033[01;37m\]\W\[\033[33m\]\$\[\033[00m\] '

alias sh='bash'
# User specific environment and startup programs
ulimit -c unlimited

PATH=$HOME/env/node/bin:${HOME}/env/nvim/bin:$PATH:$HOME/.local/bin:$HOME/bin

export PATH

export HISTSIZE=10000
export HISTFILESIZE=5000

#export JAVA_HOME=/home/disk5/sr-deps/thirdparty-latest/installed/open_jdk
export JAVA_HOME=$HOME/env/jdk-18.0.1/
#export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64/
export PYTHON_HOME=~/env/python
export GDB_HOME=~/env/gdb-13.2
export MVN_HOME=/home/disk1/sr-deps/toolchain/installed/apache-maven-3.6.3

export LD_LIBRARY_PATH=~/env/python:/usr/local/lib64/:/home/disk1/sr-deps/thirdparty-latest/installed/open_jdk/jre/lib/amd64/server/:$LD_LIBRARY_PATH
export PATH=${MVN_HOME}/bin:${JAVA_HOME}/bin:${GDB_HOME}/bin:${PYTHON_HOME}/bin:$PATH

export FLAME_HOME=~/env/Flamegragh
export PATH=${PATH}:$FLAME_HOME

export HADOOP_HOME=~/env/hadoop-2.10.0
export PATH=${PATH}:$HADOOP_HOME/bin

force_color_prompt=yes
alias ls='ls --color=auto'
alias ll='ls -l --time-style=iso'
alias dir='dir --color=auto'
alias oss='ossutil64'

export MC_DEV=172.26.92.227
export WORKSPACE=~/workspace
export SR=${WORKSPACE}/StarRocks

export UDF_RUNTIME_DIR=/tmp
export STARROCKS_HOME=$SR

export SSHPASS=sr@test

alias workspace='cd ${WORKSPACE}'
alias sr='cd ${SR}'

alias grep='grep -a --color=auto'
alias less='less -r'

alias mysr='mycli -h$MC_DEV -P8112 -uroot -p123 -D td'

alias sshp='/home/disk6/hekai/env/expect/sshp'
alias ll='ls -l'
alias rpd='echo Doris@ALI!@#'
alias vim='nvim'
alias vimdiff='nvim -d'

alias flame='perf script | stackcollapse-perf.pl | flamegraph.pl'
alias asan='python ~/env/asan/asan_symbolize.py | c++filt'

# added by Snowflake SnowSQL installer
export PATH=$HOME/hekai/snowsql:$PATH

export ASAN_OPTIONS=abort_on_error=1:disable_coredump=0:unmap_shadow_on_exit=1

export BE_SUPERVISOR=false

