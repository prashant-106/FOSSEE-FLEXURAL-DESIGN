def read_input_file():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        V = float(lines[0].strip())           # Applied shear force (V) in kN
        M = float(lines[1].strip())           # Applied moment (M) in kNm
        L = float(lines[2].strip())           # Effective span (L) in mm
        Ze = float(lines[3].strip())          # Effective section modulus (Ze) in mm³
        fy = float(lines[4].strip())          # Yield stress (fy) in MPa
        gamma_m0 = float(lines[5].strip())    # Partial safety factor for material (gamma_m0)
        beta_b = float(lines[6].strip())      # Bending coefficient (beta_b)
        A_v = float(lines[7].strip())         # Shear area (A_v) in mm²
        tau_v = float(lines[8].strip())       # Shear coefficient (tau_v)
        return V, M, L, Ze, fy, gamma_m0, beta_b, A_v, tau_v

def calculate_moment_capacity(V, M, L, Ze, fy, gamma_m0, beta_b):
    Md = (beta_b * Ze * fy) / gamma_m0
    Md_kNm = Md / 1e6  # Convert from Nmm to kNm
    
    if M <= Md_kNm:
        result = f"The applied moment is safe. Moment capacity (Md): {Md_kNm:.2f} kNm, Applied moment (M): {M} kNm."
    else:
        required_Ze = (M * gamma_m0) / (beta_b * fy) * 1e6  # Calculate required Ze in mm³ for safety
        result = (f"The applied moment exceeds the moment capacity! Moment capacity (Md): {Md_kNm:.2f} kNm, "
                  f"Applied moment (M): {M} kNm.\n"
                  f"To be safe, increase the section modulus (Ze) to at least {required_Ze:.2f} mm³.")
    return result

def calculate_shear_capacity(V, A_v, fy, gamma_m0, tau_v):
    Vd = (tau_v * A_v * fy) / gamma_m0
    Vd_kN = Vd / 1e3  # Convert from N to kN
    
    if V <= Vd_kN:
        result = f"The applied shear force is safe. Shear capacity (Vd): {Vd_kN:.2f} kN, Applied shear (V): {V} kN."
    else:
        required_A_v = (V * gamma_m0) / (tau_v * fy) * 1e3  # Calculate required A_v in mm² for safety
        result = (f"The applied shear force exceeds the shear capacity! Shear capacity (Vd): {Vd_kN:.2f} kN, "
                  f"Applied shear (V): {V} kN.\n"
                  f"To be safe, increase the shear area (A_v) to at least {required_A_v:.2f} mm².")
    return result

def check_beam_deflection(M, V, L):
    E_MPa = 200000  # Modulus of Elasticity for steel in MPa
    E_Nmm2 = E_MPa * 1e6  # Convert E to N/mm²
    I_mm4 = 8000000  # Assumed Moment of Inertia in mm⁴ (based on typical I-section)
    A_mm2 = 5000  # Assumed cross-sectional area in mm²
    K = 1.2  # Shear form factor (approximate)
    poisson_ratio = 0.3  # Typical value for steel
    G_Nmm2 = E_Nmm2 / (2 * (1 + poisson_ratio))  # Shear modulus in N/mm²
    
    # Convert inputs to consistent units
    moment_Nmm = M * 1e6  # Convert moment to Nmm
    shear_N = V * 1e3  # Convert shear to N
    
    # IS 800 permissible deflection limit (L/300 for simply supported beams)
    permissible_deflection_mm = L / 300
    
    # Calculate bending deflection
    bending_deflection_mm = (moment_Nmm * L**2) / (8 * E_Nmm2 * I_mm4)
    
    # Calculate shear deflection
    shear_deflection_mm = (shear_N * L) / (K * A_mm2 * G_Nmm2)
    
    # Total deflection
    total_deflection_mm = bending_deflection_mm + shear_deflection_mm
    
    # Check safety condition
    is_safe = total_deflection_mm <= permissible_deflection_mm
    
    # Recommendation if not safe
    recommendation = ""
    if not is_safe:
        recommendation = (
            "The total deflection exceeds the permissible limit per IS 800:2007. "
            "Consider increasing the Moment of Inertia (I) by using a larger section, "
            "or reducing the span length to ensure safety."
        )
    
    return {
        "Bending Deflection (mm)": bending_deflection_mm,
        "Shear Deflection (mm)": shear_deflection_mm,
        "Total Deflection (mm)": total_deflection_mm,
        "Permissible Deflection (mm)": permissible_deflection_mm,
        "Is Safe": "Yes" if is_safe else "No",
        "Recommendation": recommendation if not is_safe else "Beam design is within permissible limits."
    }

def write_output_file(moment_result, shear_result, deflection_result):
    with open('output.txt', 'w') as file:
        file.write(moment_result + "\n\n")
        file.write(shear_result + "\n\n")
        file.write(f"Deflection Results:\n")
        for key, value in deflection_result.items():
            file.write(f"{key}: {value}\n")

def main():
    # Read inputs from the input file
    V, M, L, Ze, fy, gamma_m0, beta_b, A_v, tau_v = read_input_file()
    
    # Perform calculations
    moment_result = calculate_moment_capacity(V, M, L, Ze, fy, gamma_m0, beta_b)
    shear_result = calculate_shear_capacity(V, A_v, fy, gamma_m0, tau_v)
    deflection_result = check_beam_deflection(M, V, L)
    
    # Write results to the output file
    write_output_file(moment_result, shear_result, deflection_result)

    # Print results to console
    print(moment_result)
    print(shear_result)
    for key, value in deflection_result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
