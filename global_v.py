import torch
from rich.console import Console


dtype = None
device = None
n_steps = None
partial_a = None
tau_s = None
console = Console()

def init(dty, dev, n_t, ts):
    global dtype, device, n_steps, partial_a, tau_s
    dtype = dty
    device = dev
    n_steps = n_t
    tau_s = ts
    partial_a = torch.zeros((1, 1, 1, 1, n_steps, n_steps), dtype=dtype).to(device)
    for t in range(n_steps):
        if t > 0:
            partial_a[..., t] = partial_a[..., t - 1] - partial_a[..., t - 1] / tau_s 
        partial_a[..., t, t] = 1/tau_s