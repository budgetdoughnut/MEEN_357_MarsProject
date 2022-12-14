import subfunctions as sf
import numpy as np
import matplotlib.pyplot as plt

planet, power_subsys, science_payload, chassis, motor, speed_reducer, wheel, wheel_assembly, rover = sf.create_dictionary()

omega_NL = 3.8
omegain = np.linspace(0, omega_NL, 100)
omega = omegain / sf.get_gear_ratio(speed_reducer)

tau = sf.tau_dcmotor(omegain, motor) * sf.get_gear_ratio(speed_reducer)
power = omega * tau

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.subplots_adjust(hspace = .5)
fig.tight_layout()
fig.suptitle('Speed Reducer Speed / Torque / Power Curves', fontsize = 10)

ax1.plot(tau, omega)
ax1.set_xlabel('SR Torque [Nm]')
ax1.set_ylabel('SR Speed [rad/s]')


ax2.plot(tau, power)
ax2.set_xlabel('SR Torque [Nm]')
ax2.set_ylabel('SR Power [W]')

ax3.plot(omega, power)
ax3.set_xlabel('SR Speed (rad/s)')
ax3.set_ylabel('SR Power [W]')

print(sf.tau_dcmotor(omega, motor))

print(np.linspace(0,omega_NL, 100))
print(omega)