Summary:	Toolbar for false User-Agent: header
Summary(pl):	Pasek narz�dziowy do fa�szowania identyfikacji przegl�darki
Name:		mozilla-addon-uabar
%define		_realname	uabar
Version:	0.1.0
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://uabar.mozdev.org/%{_realname}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://uabar.mozdev.org/
BuildRequires:	unzip
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
A toolbar that allows using false browser identify (User-Agent
header).

%description -l pl
Pasek narz�dziowy do fa�szowania identyfikacji przegl�darki (nag��wka
User-Agent).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}
rm -rf $RPM_BUILD_ROOT%{_chromedir}/%{_realname}/CVS
rm -rf $RPM_BUILD_ROOT%{_chromedir}/%{_realname}/content/CVS
rm -rf $RPM_BUILD_ROOT%{_chromedir}/%{_realname}/content/*~

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/%{_realname}-installed-chrome.txt
