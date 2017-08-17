%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname karborclient
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-karborclient
Version:        XXX
Release:        XXX
Summary:        Python API and CLI for OpenStack Karbor

License:        ASL 2.0
URL:            http://github.com/openstack/python-karborclient
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch


%description
This is a client for the OpenStack Karbor API. It provides a Python API (the
karborclient module) and a command-line interface (Karbor).

%package -n python2-%{sname}
Summary:        Python API and CLI for OpenStack Karbor
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires:  openstack-macros
BuildRequires:  python-babel
BuildRequires:  python-prettytable
BuildRequires:  python-devel
BuildRequires:  python-fixtures
BuildRequires:  python-keystoneauth1
BuildRequires:  python-mock
BuildRequires:  python-os-testr
BuildRequires:  python-osc-lib
BuildRequires:  python-oslo-i18n
BuildRequires:  python-oslo-log
BuildRequires:  python-oslo-utils
BuildRequires:  python-oslotest
BuildRequires:  python-pbr
BuildRequires:  python-subunit
BuildRequires:  python-requests
BuildRequires:  python-requests-mock
BuildRequires:  python-simplejson
BuildRequires:  python-testtools

Requires:       python-babel
Requires:       python-prettytable
Requires:       python-keystoneauth1
Requires:       python-osc-lib
Requires:       python-oslo-i18n
Requires:       python-oslo-log
Requires:       python-oslo-utils
Requires:       python-pbr
Requires:       python-requests
Requires:       python-simplejson
Requires:       python-six

%description -n python2-%{sname}
This is a client for the OpenStack Karbor API. It provides a Python API (the
karborclient module) and a command-line interface (Karbor).


%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:        Python API and CLI for OpenStack Karbor
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:  openstack-macros
BuildRequires:  python3-babel
BuildRequires:  python3-prettytable
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-mock
BuildRequires:  python3-os-testr
BuildRequires:  python3-osc-lib
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-subunit
BuildRequires:  python3-requests
BuildRequires:  python3-requests-mock
BuildRequires:  python3-simplejson
BuildRequires:  python3-testtools

Requires:       python3-babel
Requires:       python3-prettytable
Requires:       python3-keystoneauth1
Requires:       python3-osc-lib
Requires:       python3-oslo-i18n
Requires:       python3-oslo-log
Requires:       python3-oslo-utils
Requires:       python3-pbr
Requires:       python3-requests
Requires:       python3-simplejson
Requires:       python3-six

%description -n python3-%{sname}
This is a client for the OpenStack Karbor API. It provides a Python API (the
karborclient module) and a command-line interface (Karbor).
%endif


%package doc
Summary:        Documentation for OpenStack Karbor API Client
Group:          Documentation
BuildRequires:  python-sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description doc
This is a client for the OpenStack Karbor API and a command-line script (karbor).
Each implements 100% of the OpenStack Karbor API.
This package contains auto-generated documentation.

%prep
%autosetup -n %{name}-%{upstream_version} -S git
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%{py2_build}
%if 0%{?with_python3}
%py3_build
%endif

%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py2_install}
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/karbor
%{python2_sitelib}/karborclient
%{python2_sitelib}/*.egg-info
%{_bindir}/karbor

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/karbor
%{python3_sitelib}/karborclient
%{python3_sitelib}/*.egg-info
%{_bindir}/karbor
%endif

%files doc
%license LICENSE
%doc doc/build/html

%changelog
