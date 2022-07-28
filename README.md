# ndx-probe-interface Extension for NWB

SpikeInterface outputs information about probes, including the probe_planar_contour which defines the polygon shape of the electrodes themselves, so to record this information in NWB, one could use the ndx-probe-interface to generate a structure that holds these details of the electrode. 

## Installation

```bash
pip install ndx-probe-extension
```


## Usage

```python
import ndx_probe_interface as npi

probe_name = "my probe" 

# On an NWB file without an ElectrodeGroup in place yet, add the Probe Device
nwbfile.add_device(npi.Probe(name=probe_name, probe_planar_contour=np.empty((1, 1)))) 

# Create the ElectrodeGroup that uses the Probe Device we just added 
nwbfile.create_electrode_group(name="my electrode group", description="a description", location='', device=nwbfile.devices[probe_name])

```

---
This extension was created using [ndx-template](https://github.com/nwb-extensions/ndx-template).
