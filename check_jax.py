import jax

devices = jax.devices()

print(devices)
for device in devices:
    print(device.device_kind)

gpu_present = any(device.device_kind == 'gpu' for device in devices)

if gpu_present:
    print("GPU is present.")
else:
    print("No GPU detected.")