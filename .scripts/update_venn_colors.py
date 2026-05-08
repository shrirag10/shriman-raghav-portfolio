import os

new_expertise_section = """
      <!-- EXPERTISE / DOMAINS SECTION -->
      <section class="flex flex-col gap-12 mt-16 mb-16" id="expertise">
        <!-- Section Header Line -->
        <div class="flex items-center gap-4">
          <div class="text-[0.65rem] font-space uppercase tracking-widest font-bold" style="color: var(--on-surface-variant);">Expertise &amp; Domains</div>
          <div class="flex-grow h-px" style="background-color: var(--outline-variant);"></div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-8 items-center">
          
          <!-- Left Column: Venn Diagram -->
          <div class="lg:col-span-6 flex justify-center overflow-visible">
            <style>
              .venn-scale { transform: scale(0.65); transform-origin: center; }
              @media (min-width: 640px) { .venn-scale { transform: scale(0.85); } }
              @media (min-width: 1024px) { .venn-scale { transform: scale(0.9); } }
              @media (min-width: 1280px) { .venn-scale { transform: scale(1); } }
            </style>
            <div class="relative flex items-center justify-center venn-scale" style="width: 450px; height: 450px;">
              <div class="relative w-full h-full flex items-center justify-center">
                <!-- Center circle/text -->
                <div class="absolute z-10 text-center flex flex-col items-center justify-center rounded-full border-2 border-dashed backdrop-blur-sm" style="width: 12rem; height: 12rem; border-color: var(--primary); background-color: color-mix(in srgb, var(--surface) 80%, transparent);">
                  <div class="font-space font-bold tracking-[0.3em] text-xl" style="color: var(--primary);">S H R I</div>
                  <div class="font-bold text-[0.7rem] mt-1 tracking-widest" style="color: var(--primary);">MOBILE ROBOTS</div>
                  <div class="text-[0.65rem] mt-2 leading-tight" style="color: var(--on-surface-variant);">AMR Deployment<br>Path Planning</div>
                </div>
                
                <!-- AI/ML/DL/RL (Top Left) -->
                <div class="absolute rounded-full border border-dashed flex flex-col items-start justify-start pt-12 pl-12 text-center" style="width: 17rem; height: 17rem; transform: translate(-3.5rem, -3.5rem); border-color: var(--primary); background: radial-gradient(circle, color-mix(in srgb, var(--primary) 10%, transparent) 0%, color-mix(in srgb, var(--primary) 2%, transparent) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1" style="color: var(--primary);">AI/ML/DL/RL</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Deep Learning<br>Reinforcement Learning</div>
                </div>

                <!-- AV / CV (Top Right) -->
                <div class="absolute rounded-full border border-dashed flex flex-col items-end justify-start pt-12 pr-12 text-center" style="width: 17rem; height: 17rem; transform: translate(3.5rem, -3.5rem); border-color: var(--primary); background: radial-gradient(circle, color-mix(in srgb, var(--primary) 10%, transparent) 0%, color-mix(in srgb, var(--primary) 2%, transparent) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1" style="color: var(--primary);">AV / CV</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Computer Vision<br>Sensor Fusion</div>
                </div>

                <!-- HUMANOID ROBOTICS (Bottom Left) -->
                <div class="absolute rounded-full border border-dashed flex flex-col items-start justify-end pb-12 pl-12 text-center" style="width: 17rem; height: 17rem; transform: translate(-3.5rem, 3.5rem); border-color: var(--primary); background: radial-gradient(circle, color-mix(in srgb, var(--primary) 10%, transparent) 0%, color-mix(in srgb, var(--primary) 2%, transparent) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1 leading-tight" style="color: var(--primary);">HUMANOID<br>ROBOTICS</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Bipedal Locomotion<br>Control Systems</div>
                </div>

                <!-- INDUSTRIAL ENGG (Bottom Right) -->
                <div class="absolute rounded-full border border-dashed flex flex-col items-end justify-end pb-12 pr-12 text-center" style="width: 17rem; height: 17rem; transform: translate(3.5rem, 3.5rem); border-color: var(--primary); background: radial-gradient(circle, color-mix(in srgb, var(--primary) 10%, transparent) 0%, color-mix(in srgb, var(--primary) 2%, transparent) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1 leading-tight" style="color: var(--primary);">INDUSTRIAL<br>ENGG</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Manufacturing Automation<br>Process Optimization</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: Domains List -->
          <div class="lg:col-span-6 flex flex-col gap-10">
            
            <!-- AI & Deep Learning -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: color-mix(in srgb, var(--primary) 10%, transparent);">
                <span class="material-symbols-outlined" style="color: var(--primary);">psychology</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">AI &amp; Deep Learning</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Building intelligent systems that learn, adapt, and make decisions from data.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Deep Learning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Reinforcement Learning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Machine Learning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Neural Networks</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">PyTorch</span>
                </div>
              </div>
            </div>
            
            <!-- AV / CV -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: color-mix(in srgb, var(--primary) 10%, transparent);">
                <span class="material-symbols-outlined" style="color: var(--primary);">visibility</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Autonomous Vehicles &amp; CV</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Perception pipelines that let machines see and understand the world.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Computer Vision</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Sensor Fusion</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Object Detection</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">LiDAR</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">SLAM</span>
                </div>
              </div>
            </div>

            <!-- Mobile & Field Robots -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: color-mix(in srgb, var(--primary) 10%, transparent);">
                <span class="material-symbols-outlined" style="color: var(--primary);">smart_toy</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Mobile &amp; Field Robots</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Deploying robots that move, navigate, and operate in real-world environments.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">AMR Deployment</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Path Planning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">ROS</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Fleet Management</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Navigation</span>
                </div>
              </div>
            </div>

            <!-- Humanoids -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: color-mix(in srgb, var(--primary) 10%, transparent);">
                <span class="material-symbols-outlined" style="color: var(--primary);">directions_walk</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Humanoids</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">The next frontier - robots that walk, grasp, and interact like humans.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Bipedal Locomotion</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Control Systems</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Sim-to-Real</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Motion Planning</span>
                </div>
              </div>
            </div>

            <!-- Industrial Engineering -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: color-mix(in srgb, var(--primary) 10%, transparent);">
                <span class="material-symbols-outlined" style="color: var(--primary);">precision_manufacturing</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Industrial Engineering</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Bridging robotics and factory floors - real-world manufacturing impact.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Manufacturing Automation</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Process Optimization</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">PLC/HMI</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary);">Production Systems</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
"""

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# We need to replace the entire <section ... id="expertise"> block.
start_str = '<!-- EXPERTISE / DOMAINS SECTION -->'
end_str = '<!-- PERSONAL INTERESTS -->'

if start_str in content and end_str in content:
    before = content.split(start_str)[0]
    after = end_str + content.split(end_str)[1]
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(before + new_expertise_section + "\n      " + after)
    print("Updated colors and layout successfully.")
else:
    print("Could not find the target section to replace.")
