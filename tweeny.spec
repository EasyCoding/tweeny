%global commit0 43f4130f7e4a67c19d870b60864bc2862c19b81f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20180504

Name: tweeny
Summary: Modern C++ tweening library
Version: 2
Release: 0.1.%{date}git%{shortcommit0}%{?dist}

License: MIT
URL: https://github.com/mobius3/%{name}
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

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
%autosetup -n %{name}-%{commit0} -p1
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
* Wed Jul 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2-0.1.20180504git43f4130
- Initial SPEC release.
