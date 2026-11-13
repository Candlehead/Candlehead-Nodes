"""
Metadata Parse from Text Node
Parses metadata from imported text and exports specific fields
"""

import re


class MetadataParseFromText:
    """
    Parses metadata information from a text body and extracts:
    - Prompt
    - VAE Name
    - CFG
    - Sampler Name
    - Scheduler
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING",),
            },
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING", "FLOAT", "INT", "STRING", "STRING", "STRING", "INT", "INT")
    RETURN_NAMES = ("Prompt", "VAE Name", "Checkpoint/Unet", "CFG", "Steps", "Sampler Name", "Scheduler", "Summary", "Height", "Width")
    FUNCTION = "parse_metadata"
    CATEGORY = "text/metadata"
    OUTPUT_NODE = True
    
    def parse_metadata(self, text):
        """Parse metadata from text input"""
        
        # Initialize all fields as empty strings
        prompt = ""
        vae_name = ""
        checkpoint_name = ""  # Initialize checkpoint name
        cfg = 0.0  # Initialize as float
        sampler_name = ""
        scheduler = ""
        steps = 0  # Initialize as integer
        
        # Parse Prompt - text following "prompt": and capture everything in quotes including commas
        # Pattern: "prompt": "some text, with, commas" or "prompt":"text"
        prompt_match = re.search(r'"?prompt"?\s*:\s*["\']([^"\']*)["\']', text, re.IGNORECASE)
        if not prompt_match:
            # Fallback to "text": if "prompt" isn't present
            prompt_match = re.search(r'"?text"?\s*:\s*["\']([^"\']*)["\']', text, re.IGNORECASE)
        if prompt_match:
            prompt = prompt_match.group(1).strip()
        
        # Parse VAE Name - text in quotes following "vae_name":
        # Pattern: "vae_name": "value"
        vae_match = re.search(r'"?vae_name"?\s*:\s*["\']([^"\']+)["\']', text, re.IGNORECASE)
        if vae_match:
            vae_name = vae_match.group(1).strip()
        
        # Pattern: "checkpoint_name": "value"
        checkpoint_match = re.search(r'"?ckpt_name"?\s*:\s*["\']([^"\']+)["\']', text, re.IGNORECASE)
        if checkpoint_match:
            checkpoint_name = checkpoint_match.group(1).strip()
        if not checkpoint_name:
            unet_match = re.search(r'"?unet_name"?\s*:\s*["\']([^"\']+)["\']', text, re.IGNORECASE)
            if unet_match:
                checkpoint_name = unet_match.group(1).strip()
        
        # Parse CFG - text in quotes following "cfg":
        # Pattern: "cfg": "value" - extract numeric value
        cfg_match = re.search(r'"?cfg"?\s*:\s*["\']?([0-9.]+)["\']?', text, re.IGNORECASE)
        if cfg_match:
            try:
                cfg = float(cfg_match.group(1).strip())
            except ValueError:
                cfg = 0.0
        
        # Parse Sampler Name - text in quotes following "sampler_name":
        # Pattern: "sampler_name": "value"
        sampler_match = re.search(r'"?sampler_name"?\s*:\s*["\']([^"\']+)["\']', text, re.IGNORECASE)
        if sampler_match:
            sampler_name = sampler_match.group(1).strip()
        
        # Parse Scheduler - text in quotes following "scheduler":
        # Pattern: "scheduler": "value"
        scheduler_match = re.search(r'"?scheduler"?\s*:\s*["\']([^"\']+)["\']', text, re.IGNORECASE)
        if scheduler_match:
            scheduler = scheduler_match.group(1).strip()
        
        # Parse Steps - numerical value in quotes following "steps":
        # Pattern: "steps": "value" or "steps": value
        steps_match = re.search(r'"?steps"?\s*:\s*["\']?([0-9]+)["\']?', text, re.IGNORECASE)
        if steps_match:
            try:
                steps = int(steps_match.group(1).strip())
            except ValueError:
                steps = 0

        # Parse Height - numerical value in quotes following "height":
        # Pattern: "height": "value" or "height": value
        height_match = re.search(r'"?height"?\s*:\s*([0-9]{3,4})', text, re.IGNORECASE)
        height = 0
        if height_match:
            try:
                height = int(height_match.group(1).strip())
            except ValueError:
                height = 0

        # Parse Width - numerical value in quotes following "width":
        # Pattern: "width": "value" or "width": value
        width_match = re.search(r'"?width"?\s*:\s*([0-9]{3,4})', text, re.IGNORECASE)
        width = 0
        if width_match:
            try:
                width = int(width_match.group(1).strip())
            except ValueError:
                width = 0

        
        
        # Format summary display
        summary = (
            f"Prompt: {prompt}\n"
            f"Checkpoint Name: {checkpoint_name}\n"
            f"VAE Name: {vae_name}\n"
            f"CFG: {cfg}\n"
            f"Sampler Name: {sampler_name}\n"
            f"Scheduler: {scheduler}\n"
            f"Steps: {steps}\n"
            f"Resolution: {width}(W)x{height}(H)"
        )
        
        return (prompt, vae_name, checkpoint_name, cfg, steps, sampler_name, scheduler, summary, height, width)
