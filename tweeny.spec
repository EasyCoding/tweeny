# This is a header-only library, but it install also cmake
# scripts to %%{_libdir}, so it cannot be noarch.
%global debug_package %{nil}

Name: tweeny
Summary: Modern C++ tweening library
Version: 3
Release: 3%{?dist}

License: MIT
URL: https://github.com/mobius3/%{name}
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
mkdir -p %{_target_platform}
sed -i 's@lib/@%{_libdir}/@g' cmake/SetupExports.cmake

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DTWEENY_BUILD_EXAMPLES=OFF \
    -DTWEENY_BUILD_DOCUMENTATION=OFF \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files devel
%doc README.md CHANGELOG.md
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/cmake/Tweeny

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3-1
- Updated to version 3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-2.20180504git43f4130
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2-1.20180504git43f4130
- Initial SPEC release.
