Summary:        Toolbar for false User-Agent: header
Summary(pl):    Pasek narzêdziowy do fa³szowania identyfikacji przegl±darki
Name:           mozilla-addon-uabar
Version:        0.1.0
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://uabar.mozdev.org/uabar.xpi
Source1:        uabar-installed-chrome.txt
URL:            http://uabar.mozdev.org/
BuildRequires:  unzip
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	uabar

%description
%description -l pl
Pasek narzêdziowy do fa³szowania identyfikacji przegl±darki (nag³ówka User-Agent:)


%prep
%setup -q -c -T
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
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "%{_realname}" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/%{_realname}-installed-chrome.txt
