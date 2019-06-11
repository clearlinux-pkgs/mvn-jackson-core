#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jackson-core
Version  : 2.1.5
Release  : 2
URL      : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.jar
Source0  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.jar
Source1  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.pom
Source2  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/4/oss-parent-4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jackson-core-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jackson-core package.
Group: Data

%description data
data components for the mvn-jackson-core package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/4


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/4/oss-parent-4.pom
