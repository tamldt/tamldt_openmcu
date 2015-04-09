# spec file for openmcu-ru
%define name 		openmcu-ru
%define version		
%define release 	
%define arch		
%define _target_cpu	%{arch}
%define buildroot	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{arch}

# disable binary stripping
%define __os_install_post %{nil}

BuildRoot:	%{buildroot}
Summary:	OpenMCU-ru video conference server
Vendor:		OpenMCU-ru Team
URL:		http://openmcu.ru
Packager:	
License:	MPL, GPL
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System Environment/Daemons
Autoprov:	0
#Provides:	openmcu-ru
Autoreq:	0
Requires:	
%description
OpenMCU-ru - H.323/SIP/RTSP Multipoint Control Unit for video conferences.

#%prep

#%build
#./configure
#make

#%install
#make install

%files
%config(noreplace) /opt/openmcu-ru/config
%config(noreplace) /opt/openmcu-ru/scripts
/etc/rc.d/init.d/openmcu-ru
/opt/openmcu-ru

%post
DAEMON_USER="mcu"
DAEMON_NAME="openmcu-ru"
DAEMON_HOMEDIR="/opt/openmcu-ru"
# Creating system user
adduser --home-dir $DAEMON_HOMEDIR -M -r $DAEMON_USER
# Creating home directory
chmod 0700 $DAEMON_HOMEDIR
chown $DAEMON_USER: $DAEMON_HOMEDIR
chown $DAEMON_USER: $DAEMON_HOMEDIR/config
chown $DAEMON_USER: $DAEMON_HOMEDIR/log
chown $DAEMON_USER: $DAEMON_HOMEDIR/pipe
chown $DAEMON_USER: $DAEMON_HOMEDIR/records
# Service
chkconfig --add openmcu-ru
service openmcu-ru start
exit 0

%preun
DAEMON_USER="mcu"
DAEMON_NAME="openmcu-ru"
DAEMON_PIDDIR="/var/run/$DAEMON_NAME"
# Service
service openmcu-ru stop
chkconfig --del openmcu-ru
# Delete system user
userdel $DAEMON_USER
# Delete pid directory
rm -rf $DAEMON_PIDDIR >/dev/null 2>&1
exit 0

%postun
exit 0
