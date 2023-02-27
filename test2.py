import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "./stable-diffusion-2-1-base"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.to("cuda")
pipe.enable_attention_slicing()

prompt = "a photo of an astronaut riding a horse on mars"
seed = 200
num_images_per_prompt = 5

generator = torch.manual_seed(seed)
images = pipe(
    prompt = prompt,
    generator = generator,
    num_images_per_prompt = num_images_per_prompt).images

for i, image in enumerate(images):
    image.save(f"result_{i}.png").git
