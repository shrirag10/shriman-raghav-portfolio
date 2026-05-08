import os

html_snippet = """
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
            <div class="relative w-[450px] h-[450px] flex items-center justify-center venn-scale">
              <div class="relative w-full h-full flex items-center justify-center">
                <!-- Center circle/text -->
                <div class="absolute z-10 text-center flex flex-col items-center justify-center w-48 h-48 rounded-full border-2 border-dashed backdrop-blur-sm" style="border-color: var(--primary); background-color: color-mix(in srgb, var(--surface) 60%, transparent);">
                  <div class="font-space font-bold tracking-[0.3em] text-xl" style="color: var(--primary);">S H R I</div>
                  <div class="font-bold text-[0.7rem] mt-1 tracking-widest" style="color: var(--primary);">MOBILE ROBOTS</div>
                  <div class="text-[0.65rem] mt-2 leading-tight" style="color: var(--on-surface-variant);">AMR Deployment<br>Path Planning</div>
                </div>
                
                <!-- AI/ML/DL/RL (Top Left) -->
                <div class="absolute w-[17rem] h-[17rem] rounded-full border border-dashed flex flex-col items-start justify-start pt-14 pl-12 text-center -translate-x-16 -translate-y-16" style="border-color: #8b5cf6; background: radial-gradient(circle, rgba(139,92,246,0.15) 0%, rgba(139,92,246,0.02) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1" style="color: #8b5cf6;">AI/ML/DL/RL</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Deep Learning<br>Reinforcement Learning</div>
                </div>

                <!-- AV / CV (Top Right) -->
                <div class="absolute w-[17rem] h-[17rem] rounded-full border border-dashed flex flex-col items-end justify-start pt-16 pr-12 text-center translate-x-16 -translate-y-12" style="border-color: #10b981; background: radial-gradient(circle, rgba(16,185,129,0.15) 0%, rgba(16,185,129,0.02) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1" style="color: #10b981;">AV / CV</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Computer Vision<br>Sensor Fusion</div>
                </div>

                <!-- HUMANOID ROBOTICS (Bottom Left) -->
                <div class="absolute w-[17rem] h-[17rem] rounded-full border border-dashed flex flex-col items-start justify-end pb-16 pl-10 text-center -translate-x-12 translate-y-16" style="border-color: #f59e0b; background: radial-gradient(circle, rgba(245,158,11,0.15) 0%, rgba(245,158,11,0.02) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1 leading-tight" style="color: #f59e0b;">HUMANOID<br>ROBOTICS</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Bipedal Locomotion<br>Control Systems</div>
                </div>

                <!-- INDUSTRIAL ENGG (Bottom Right) -->
                <div class="absolute w-[17rem] h-[17rem] rounded-full border border-dashed flex flex-col items-end justify-end pb-14 pr-12 text-center translate-x-16 translate-y-20" style="border-color: #a855f7; background: radial-gradient(circle, rgba(168,85,247,0.15) 0%, rgba(168,85,247,0.02) 100%);">
                  <div class="w-full font-bold text-[0.8rem] mb-1 leading-tight" style="color: #a855f7;">INDUSTRIAL<br>ENGG</div>
                  <div class="w-full text-[0.65rem] leading-tight" style="color: var(--on-surface-variant);">Manufacturing Automation<br>Process Optimization</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: Domains List -->
          <div class="lg:col-span-6 flex flex-col gap-10">
            
            <!-- AI & Deep Learning -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: rgba(139,92,246,0.15);">
                <span class="material-symbols-outlined" style="color: #8b5cf6;">psychology</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">AI &amp; Deep Learning</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Building intelligent systems that learn, adapt, and make decisions from data.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(139,92,246,0.1); color: #8b5cf6;">Deep Learning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(139,92,246,0.1); color: #8b5cf6;">Reinforcement Learning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(139,92,246,0.1); color: #8b5cf6;">Machine Learning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(139,92,246,0.1); color: #8b5cf6;">Neural Networks</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(139,92,246,0.1); color: #8b5cf6;">PyTorch</span>
                </div>
              </div>
            </div>
            
            <!-- AV / CV -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: rgba(16,185,129,0.15);">
                <span class="material-symbols-outlined" style="color: #10b981;">visibility</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Autonomous Vehicles &amp; CV</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Perception pipelines that let machines see and understand the world.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(16,185,129,0.1); color: #10b981;">Computer Vision</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(16,185,129,0.1); color: #10b981;">Sensor Fusion</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(16,185,129,0.1); color: #10b981;">Object Detection</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(16,185,129,0.1); color: #10b981;">LiDAR</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(16,185,129,0.1); color: #10b981;">SLAM</span>
                </div>
              </div>
            </div>

            <!-- Mobile & Field Robots -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: rgba(239,68,68,0.15);">
                <span class="material-symbols-outlined" style="color: #ef4444;">smart_toy</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Mobile &amp; Field Robots</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Deploying robots that move, navigate, and operate in real-world environments.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(239,68,68,0.1); color: #ef4444;">AMR Deployment</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(239,68,68,0.1); color: #ef4444;">Path Planning</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(239,68,68,0.1); color: #ef4444;">ROS</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(239,68,68,0.1); color: #ef4444;">Fleet Management</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(239,68,68,0.1); color: #ef4444;">Navigation</span>
                </div>
              </div>
            </div>

            <!-- Humanoids -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: rgba(245,158,11,0.15);">
                <span class="material-symbols-outlined" style="color: #f59e0b;">directions_walk</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Humanoids</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">The next frontier - robots that walk, grasp, and interact like humans.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(245,158,11,0.1); color: #f59e0b;">Bipedal Locomotion</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(245,158,11,0.1); color: #f59e0b;">Control Systems</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(245,158,11,0.1); color: #f59e0b;">Sim-to-Real</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(245,158,11,0.1); color: #f59e0b;">Motion Planning</span>
                </div>
              </div>
            </div>

            <!-- Industrial Engineering -->
            <div class="flex gap-5 items-start">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background-color: rgba(168,85,247,0.15);">
                <span class="material-symbols-outlined" style="color: #a855f7;">precision_manufacturing</span>
              </div>
              <div class="flex flex-col gap-2">
                <h3 class="font-bold text-[1.05rem]" style="color: var(--on-surface);">Industrial Engineering</h3>
                <p class="text-[0.85rem]" style="color: var(--on-surface-variant);">Bridging robotics and factory floors - real-world manufacturing impact.</p>
                <div class="flex flex-wrap gap-2 mt-1">
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(168,85,247,0.1); color: #a855f7;">Manufacturing Automation</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(168,85,247,0.1); color: #a855f7;">Process Optimization</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(168,85,247,0.1); color: #a855f7;">PLC/HMI</span>
                  <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold" style="background-color: rgba(168,85,247,0.1); color: #a855f7;">Production Systems</span>
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

# Target insertion point: Before "<!-- PERSONAL INTERESTS -->"
target = "      <!-- PERSONAL INTERESTS -->"
if target in content:
    content = content.replace(target, html_snippet + target)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print("Injected expertise section successfully.")
else:
    print("Could not find the target section to insert.")
