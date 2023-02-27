import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from huggingface_hub import snapshot_download
snapshot_download(repo_id="stabilityai/stable-diffusion-2-1-base", revision="main")


model_id = "./stable-diffusion-2-1-base"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.to("cuda")
pipe.enable_attention_slicing()

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]
    
image.save("astronaut_rides_horse.png")
