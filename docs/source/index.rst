**************
STAC Generator
**************

:fa:`github` `View on Github <https://github.com/cedadev/stac-generator>`_

The STAC Generator provides the framework and access to shared tools. The framework
allows you to build generators to get metadata from file objects using plugins to
change the source of the files, the output of the metadata and the processing chain
which extracts the metadata. The framework leverages a modular, plugin architecture
to allow users to modify the workflow to fit their needs.

The process expects a stream of "assets" (an asset being a file, zarr object, etc.).
The source of this stream is configured with `input plugins <stac_generator/inputs>`_
which could be as simple as listing directories on a file system or using message
queues as part of a complex ingest system. The `generators <generators>`_ operate on this stream and
pass to `output plugins <stac_generator/outputs>`_. The output is at the level
of an "asset" so higher level aggregated objects may require an aggregation step.

These outputs are also configurable so could dump to the terminal (for debugging), file,
a data store (postgres, elasticsearch, etc.) or even a message queue for onward processing.

.. image:: images/stac_generator_diagram.png

The framework was constructed to extract metadata for creating STAC catalogs
but could be used to extract metadata for any faceted search system.

What is STAC?
==============

The SpatioTemporal Asset Catalog (`STAC <https://stacspec.org/>`_) specification provides a common language to
describe a range of geospatial information, so it can more easily be indexed and discovered.
A "spatiotemporal asset" is any file that represents information about the earth captured
in a certain space and time.

Generators
==========

The different generators are designed to extract different levels of metadata to build the assets, items, and collections of the STAC Catalog.

.. list-table::
    :header-rows: 1

    * - Name
      - Description
    * - :ref:`Asset Generator <stac_generator/generators:asset>`
      - Generates STAC Assets via extraction methods specified in the :ref:`colelction descriptions <collection_descriptions/collection_descriptions:collection descriptions>`
      focusing on file metadata (name, location, size, etc.)
    * - :ref:`Item Generator <item_generator/generators:item>`
      - Generates STAC Items via extraction methods specified in the :ref:`colelction descriptions <collection_descriptions/collection_descriptions:collection descriptions>`
      focusing on aggregation from asset metadata.
    * - :ref:`Collection Generator <stac_generator/generators:collection>`
      - Generates STAC Collections via extraction methods specified in the :ref:`colelction descriptions <collection_descriptions/collection_descriptions:collection descriptions>`
      focusing on aggregation from item metadata.



.. toctree::
   :maxdepth: 3
   :caption: Contents:

   stac_generator/index
   collection_descriptions/collection_descriptions

.. toctree::
   :maxdepth: 2
   :caption: API:

   api/stac_generator/stac_generator


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
