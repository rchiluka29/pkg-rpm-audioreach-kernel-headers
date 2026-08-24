%global debug_package %{nil}
%global commit      bf478f88d42068a9bd90cbd8162171acce8114d6
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global commitdate  20260422

Name:           audioreach-kernel-headers
Version:        0^%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        AudioReach kernel UAPI headers
License:        GPL-2.0-only
URL:            https://github.com/AudioReach/audioreach-kernel
Source0:        https://github.com/AudioReach/audioreach-kernel/archive/%{commit}/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

%description
AudioReach kernel UAPI headers for interfacing userspace audio
components with the AudioReach kernel audio driver.
Provides msm_audio.h for use by AudioReach userspace packages.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build - header files only

%install
install -d %{buildroot}%{_includedir}/linux
cp -fr include/uapi/linux/* %{buildroot}%{_includedir}/linux/
install -d %{buildroot}%{_includedir}/dsp
cp -fr include/dsp/* %{buildroot}%{_includedir}/dsp/

%files
%license LICENSE
%{_includedir}/linux/*
%{_includedir}/dsp/*

%changelog
* Wed Apr 22 2026 Qualcomm Linux <quic_linux@quicinc.com> - 0^20260422gitbf478f88-1
- Initial RPM packaging of AudioReach kernel UAPI headers
