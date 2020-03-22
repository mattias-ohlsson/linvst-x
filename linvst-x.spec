%global debug_package %{nil}

Name:           linvst-x
Version:        2.7
Release:        1%{?dist}
Summary:        Windows VST wrapper for Linux

License:        GPLv3+
URL:            https://github.com/osxmidi/LinVst-X
Source0:        https://github.com/osxmidi/LinVst-X/archive/%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  wine-devel libX11-devel
BuildRequires:  glibc-devel(x86-32)
Requires:       wine

%description
LinVst-X runs Windows VST plugins in a single Wine process so plugins that
communicate with each other or plugins that can use shared samples between
instances will be able to communicate with their other instances.

%prep
%autosetup -n LinVst-X-%{version}

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

install -D -p vst/linvstx.so %{buildroot}%{_datadir}/%{name}/linvstx.so

%files
%license COPYING
%doc README.md
%{_bindir}/lin-vst-server-x32.exe
%{_bindir}/lin-vst-server-x32.exe.so
%{_bindir}/lin-vst-server-x.exe
%{_bindir}/lin-vst-server-x.exe.so
%{_datadir}/%{name}/linvstx.so

%changelog
* Sun Mar 22 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.7-1
- Initial build
