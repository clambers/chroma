ZFLAGS = -ur
XLFLAGS = --dropdtd --noent

SOURCES = $(srcdir)/index.html
CONFIG = chroma.xml
TARGET = $(PACKAGE_NAME).wgt

BUILT_SOURCES = $(srcdir)/config.xml
EXTRA_DIST = $(BUILT_SOURCES) $(SOURCES)

CLEANFILES = $(TARGET)
MAINTAINERCLEANFILES = $(BUILT_SOURCES)

ZFLAGS_V = $(ZFLAGS_V_@AM_V@)
ZFLAGS_V_ = $(ZFLAGS) -q
ZFLAGS_V_0 = $(ZFLAGS)

all: $(BUILT_SOURCES) $(TARGET)

$(TARGET): $(SOURCES)
	$(AM_V_GEN) $(ZIP) $(ZFLAGS_V) $@ $(BUILT_SOURCES) $(SOURCES)

config.xml: $(top_srcdir)/configure.ac $(CONFIG).in
	$(AM_V_GEN) $(XML_LINT) $(XLFLAGS) $(CONFIG) > $@
