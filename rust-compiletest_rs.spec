# Generated by rust2rpm 12
%bcond_without check
%global debug_package %{nil}

%global crate compiletest_rs

Name:           rust-%{crate}
Version:        0.4.0
Release:        2%{?dist}
Summary:        Compiletest utility from the Rust compiler as a standalone testing harness

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/compiletest_rs
Source:         %{crates_source}
# Initial patched metadata
# * Remove Windows-only dependency
Patch0:         compiletest_rs-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Compiletest utility from the Rust compiler as a standalone testing harness.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-devel %{_description}

This package contains library source intended for building other packages
which use "rustc" feature of "%{crate}" crate.

%files       -n %{name}+rustc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stable-devel %{_description}

This package contains library source intended for building other packages
which use "stable" feature of "%{crate}" crate.

%files       -n %{name}+stable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tempfile-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tempfile-devel %{_description}

This package contains library source intended for building other packages
which use "tempfile" feature of "%{crate}" crate.

%files       -n %{name}+tempfile-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tmp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tmp-devel %{_description}

This package contains library source intended for building other packages
which use "tmp" feature of "%{crate}" crate.

%files       -n %{name}+tmp-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 02:54:03 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Initial package
