#! /bin/bash
# Author: Escape
# Date & Time: 2016-05-05 23:47:07
# Description:
#    This script is responsible to configure the basic run conditions and
# the initial setting, so mainly divides into the following several. Bec-
# ause the configuration process was opposite in the novice, was quite d-
# ifficult, therefore here used the script to carry on the configuration,
# simplify operation.
#       1. install and config ==> pip
#       2. install and config ==> pcap
#       3. install and config ==> pyenv
#       ( suitable in Centos6.* )


# config export
conf_export()
{
    export INname=install_env
    export Base_Dir=/root/date_collect
    export INversion=0.0.1
    clear
}


# print header prompt
print_header()
{
    echo "###################################################################"
    echo "#                    $INname  version $INversion                  #" 
    echo "#                Author: Escape <admin@wsescape.com>              #"    
    echo "#-----------------------------------------------------------------#"
    echo "#          Welcome , start init date_collect env at now !         #"
    echo "###################################################################"
    echo 
}



# check root user by use
Check_Root()
{
    userid=$(id | awk '{print $1}' | sed -e 's/=/ /' -e 's/(/ /' -e 's/)/ /'|awk '{print $2}')
    if [[ $userid -ne 0 ]]
    then
        echo "Error: No root permissions,Please run with root user..."
        exit 1
    fi
}


# add info to bashrc
add_bashrc()
{
    if [ $# -lt 1 ] ; then
    echo "Uages: Please input one or more than arg[] ..."
    exit 1
    fi

    if ! grep "^#\!" $1 &> /dev/null ; then
    cat >> $1 << EOF
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

EOF
    fi
}


# yum install software
Yum_Install()
{
    # install system env
    echo "##### Start install system env #####"
    yum update -y >> /dev/null
    echo "[===       ]"
    vim --version >> /dev/null || yum install -y vim
    echo "[=======   ]"
    wget --version >> /dev/null || yum install -y wget
    echo "[==========]"
    echo ">>> Install system env is done !"
    echo 

    # install pip
    echo "##### Start install pip env #####"
    easy_install --version >> /dev/null || yum install -y python-setuptools
    echo "[=         ]"
    easy_install -i http://pypi.douban.com/simple pip >> /dev/null
    echo "[===       ]"
    pip install construct >> /dev/null
    echo "[=======   ]"
    pip install scapy >> /dev/null
    echo "[==========]"
    echo ">>> Install pip env is done !"
    echo

    # install pcap
    echo "##### Start install pcap env #####"
    yum install -y py*  >> /dev/null
    yum install -y gcc* >> /dev/null
    echo "[=         ]"
    yum install -y lib*  >> /dev/null
    echo "[==        ]"
    yum install bzip2 bzip2-devel -y  >> /dev/null
    echo "[===       ]"
    yum install zlib zlib-devel -y  >> /dev/null
    echo "[=====     ]"
    yum install openssl openssl-devel -y  >> /dev/null
    echo "[=======   ]"

    wget http://nchc.dl.sourceforge.net/project/pylibpcap/pylibpcap/0.6.4/pylibpcap-0.6.4.tar.gz
    tar -zxvf pylibpcap-0.6.4.tar.gz
    cd pylibpcap-0.6.4.tar.gz
    echo "[========  ]"

    python ./setup.py install >> /dev/null
    if [ $? -ne 0 ]; then
        echo "[==========]"
        echo ">>> Install pcap env is done !"
        echo
    else
        echo "Error: The pcap lib install failed, please check..."
    exit 1
    fi

    # install pyenv
    echo "##### Start install pyenv env #####"
    rpm -qa | grep -E '^(git)\.*' >> /dev/null || yum install -y git >> /dev/null
    echo "[=        ]"
    curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
    echo "[====     ]"
    add_bashrc ~/.bashrc
    echo "[========  ]"

    pyven install 2.7.6 >> /dev/null
    if [ $? -ne 0 ]; then
        echo "[==========]"
        echo ">>> Install pyenv env is done !"
        echo
    else
        echo "Error: The pyenv lib install failed, please check..."
    exit 1
    fi
}


# print footer prompt
print_footer()
{
    echo "###################################################################"
    echo "#      Congratulates you has completed the installment           #"
    echo "###################################################################"
}


# program execution entrance
main()
{
    conf_export
    print_header
    Check_Root
    Yum_Install
    print_footer
}

main
