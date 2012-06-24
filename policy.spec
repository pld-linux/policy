#
# Conditional build:
%bcond_with	selinux24	# build old SELinux-compatible policy (ver. 15)
#
Summary:	SELinux example policy configuration
Summary(pl):	Przyk�adowa konfiguracja polityki SELinuksa
Name:		policy
Version:	1.28
Release:	1
Epoch:		1
License:	GPL
Group:		Base
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	d9b5b04d823e08dec1f5710143b60741
Patch0:		%{name}-sh.patch
Patch1:		%{name}-iptables.patch
Patch2:		%{name}-postfix.patch
Patch3:		%{name}-login.patch
Patch4:		%{name}-mgetty.patch
Patch5:		%{name}-apache.patch
BuildRequires:	checkpolicy >= 1.28
BuildRequires:	policycoreutils >= 1.28
BuildRequires:	m4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		poltype		strict

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
obowi�zkowej kontroli dost�pu dla spo�eczno�ci linuksowej. Ukazuje
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
Requires:	policycoreutils >= 1.26

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
mv -f domains/program/{dpk*,gatekeeper*,qmail*,nx_server*} domains/program/unused

%build
%{__make} TYPE=%{poltype} file_contexts/file_contexts
%{__make} TYPE=%{poltype} policy

%if %{with selinux24}
# for 2.4.26+selinux or <=2.6.5
%{__make} policy \
	POLICYCOMPAT="-c 15"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-src \
	TYPE=%{poltype} \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with selinux24}
install policy.15 $RPM_BUILD_ROOT%{_sysconfdir}/selinux/%{poltype}/policy
%endif

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/selinux/%{poltype}/src/policy/{COPYING,ChangeLog,README,VERSION,policy.spec,policy.[12][0-9]}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/selinux
%dir %{_sysconfdir}/selinux/%{poltype}
%dir %{_sysconfdir}/selinux/%{poltype}/contexts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/contexts/customizable_types
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/contexts/default_type
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/contexts/*_context*
%dir %{_sysconfdir}/selinux/%{poltype}/contexts/files
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/contexts/files/file_contexts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/contexts/files/homedir_template
%{_sysconfdir}/selinux/%{poltype}/contexts/files/homedir_template
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/contexts/files/media
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/contexts/port_types
%dir %{_sysconfdir}/selinux/%{poltype}/contexts/users
%config(noreplace) %verify(not md5 mtime size) %dir %{_sysconfdir}/selinux/%{poltype}/contexts/users/root
%dir %{_sysconfdir}/selinux/%{poltype}/users
%config(noreplace) %verify(not md5 mtime size) %dir %{_sysconfdir}/selinux/%{poltype}/users/local.users
%dir %{_sysconfdir}/selinux/%{poltype}/users/system.users
%dir %{_sysconfdir}/selinux/%{poltype}/policy
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/policy/policy.*

%files sources
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_sysconfdir}/selinux/%{poltype}/src
%dir %{_sysconfdir}/selinux/%{poltype}/src/policy
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/src/policy/local.users
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/src/policy/users
%dir %{_sysconfdir}/selinux/%{poltype}/src/policy/tunables
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/selinux/%{poltype}/src/policy/tunables/*.tun
%{_sysconfdir}/selinux/%{poltype}/src/policy/[!ltu]*
%{_sysconfdir}/selinux/%{poltype}/src/policy/targeted
%{_sysconfdir}/selinux/%{poltype}/src/policy/tmp
%{_sysconfdir}/selinux/%{poltype}/src/policy/types
