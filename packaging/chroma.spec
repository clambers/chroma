Name:     Chroma
Summary:  An application for controlling Philips hue lights
Version:  1.0
Release:  1%{?dist}
Group:    Applications/Web Applications
License:  GPL-3.0
URL:      http://www.tizen.org2
Source:   %{name}-%{version}.tar.gz

BuildRequires: xmllint
BuildRequires: zip

%global wgtdir %{_datadir}/wgt

%description
Chroma is a Tizen web application that allows for controlling features of the
Philips hue light collection.

%prep
%autosetup

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%post
su app -c "pkgcmd -i -t wgt -p %{_wgtdir}/Chroma.wgt -q"

%preun
su app -c "pkgcmd -u -n Chroma -q"

%files
%defattr(-,root,root,-)
%doc README.md
%license COPYING
%{_wgtdir}/Chroma.wgt
