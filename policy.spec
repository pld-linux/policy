Summary:	SELinux example policy configuration
Summary(pl):	Przyk�adowa konfiguracja polityki SELinuksa
Name:		policy
Version:	1.10
Release:	0.3
Epoch:		1
License:	GPL
Group:		Base
# from ftp://people.redhat.com/dwalsh/SELinux/srpms/policy-%{version}-*.src.rpm
#Source0:	%{name}-%{version}.tar.bz2
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	7c36ee68efd14b001eaa28f87564b374
Patch0:		%{name}-sh.patch
Patch1:		%{name}-iptables.patch
Patch2:		%{name}-postfix.patch
Patch3:		%{name}-login.patch
Patch4:		%{name}-mgetty.patch
Patch5:		%{name}-apache.patch
BuildRequires:	checkpolicy >= 1.10
BuildRequires:	policycoreutils >= 1.10
BuildRequires:	m4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains the SELinux example policy configuration along
with the Flask configuration information and the application
configuration files.

%description -l pl
Security-enhanced Linux jest poprawk� j�dra Linuksa i wielu
aplikacji u�ytkowych o funkcjach podwy�szonego bezpiecze�stwa.
Zaprojektowany jest tak, aby w prosty spos�b ukaza� znaczenie
mandatowej kontroli dost�pu dla spo�eczno�ci Linuksowej. Ukazuje
r�wnie� jak tak� kontrol� mo�na doda� do istniej�cego systemu typu
Linux. J�dro SELinux zawiera nowe sk�adniki architektury pierwotnie
opracowane w celu ulepszenia bezpiecze�stwa systemu operacyjnego
Flask. Te elementy zapewniaj� og�lne wsparcie we wdra�aniu wielu typ�w
polityk mandatowej kontroli dost�pu, w��czaj�c te wzorowane na: Type
Enforcement, kontroli dost�pu opartej na rolach i zabezpieczeniach
wielopoziomowych.

Ten pakiet zawiera przyk�adow� konfiguracj� polityki dla SELinuksa
wraz z informacjami o konfiguracji Flask oraz plikami konfiguracyjnymi
aplikacji.

%package sources
Summary:	SELinux example policy configuration source files
Summary(pl):	Pliki �r�d�owe przyk�adowej konfiguracji polityki SELinuksa
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	m4
Requires:	make
Requires:	policycoreutils >= 1.4-4

%description sources
This subpackage includes the source files used to build the policy
configuration. Includes policy.conf and the Makefiles, macros and
source files for it.

%description sources -l pl
Ten podpakiet zawiera pliki �r�d�owe u�yte do zbudowania konfiguracji
polityki. Zawiera policy.conf oraz wszystkie Makefile, makra i pliki
�r�d�owe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

find . -name '*.orig' | xargs -r rm -f

mv -f domains/misc/unused/* domains/misc
mv -f domains/program/unused/* domains/program
mv -f domains/program/{dpk*,gatekeeper*,qmail*} domains/program/unused

%build
%{__make} file_contexts/file_contexts
%{__make} policy
%{__make} policy \
	POLICYCOMPAT="-c 16"
%{__make} policy \
	POLICYCOMPAT="-c 15"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/security/selinux

%{__make} install install-src \
	DESTDIR=$RPM_BUILD_ROOT

install policy.15 $RPM_BUILD_ROOT%{_sysconfdir}/security/selinux

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/security/selinux/src/policy/{COPYING,ChangeLog,README,VERSION,policy.spec}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/security/default_contexts
%{_sysconfdir}/security/default_type
%{_sysconfdir}/security/failsafe_context
%{_sysconfdir}/security/initrc_context
%dir %{_sysconfdir}/security/selinux
%{_sysconfdir}/security/selinux/policy.*
%{_sysconfdir}/security/selinux/file_contexts

%files sources
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_sysconfdir}/security/selinux/src
%{_sysconfdir}/security/selinux/src/policy.conf
%dir %{_sysconfdir}/security/selinux/src/policy
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/selinux/src/policy/users
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/selinux/src/policy/tunable.te
%{_sysconfdir}/security/selinux/src/policy/[!ut]*
%{_sysconfdir}/security/selinux/src/policy/types
%{_sysconfdir}/security/selinux/src/policy/tmp
