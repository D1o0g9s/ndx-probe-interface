# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec
# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""An NWB extension to handle probe interface details used  in SpikeInterface""",
        name="""ndx-probe-interface""",
        version="""0.1.0""",
        author=list(map(str.strip, """Geeling Chau""".split(','))),
        contact=list(map(str.strip, """gchau@caltech.edu""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found.
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # all types included or used by the types specified here will also be
    # included.
    ns_builder.include_type("Device", namespace="core")

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information

    probe_planar_dataset = NWBDatasetSpec(
        name="probe_planar_contour",
        doc="The planar polygon that outlines the probe contour.",
        dtype="float",
        dims=[['num_points', 'x'], ['num_points', 'x, y'], ['num_points', 'x, y, z']],
        shape=[[None,1], [None, 2], [None,3]],
        attributes=[
            NWBAttributeSpec(
                name='unit',
                doc='Unit of measurement for probe_planar_contour specifications',
                dtype='text',
                default_value='um'
            )
        ]
    )

    probe_interface = NWBGroupSpec(
        neurodata_type_def='Probe',
        neurodata_type_inc='Device',
        doc=('An extension of NWBData to include ProbeInterface details from SpikeInterface.'),
        datasets=[probe_planar_dataset],
    )

    # TODO: add all of your new data types to this list
    new_data_types = [probe_interface]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)
    print('Spec files generated. Please make sure to rerun `pip install .` to load the changes.')


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()
