Summary:	Toolbar for false User-Agent: header
Summary(pl):	Pasek narzêdziowy do fa³szowania identyfikacji przegl±darki
Name:		mozilla-addon-uabar
%define		_realname	uabar
Version:	0.1.1
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.mozdev.org/%{_realname}/%{_realname}-%{version}.xpi
# Source0-md5:	258b9335cbf1b45d2375cb04590d1dc9
Source1:	%{_realname}-installed-chrome.txt
URL:		http://uabar.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla >= 1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
A toolbar that allows using false browser identify (User-Agent
header).

%description -l pl
Pasek narzêdziowy do fa³szowania identyfikacji przegl±darki (nag³ówka
User-Agent).

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

cd %{_realname}
rm -r CVS
rm -r content/CVS
rm content/*
zip -r -9 -m ../%{_realname}.jar ./
cd -

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
