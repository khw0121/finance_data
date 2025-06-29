def CAGR(initial_value, final_value, years) :
    if initial_value <= 0 or final_value <=0 or years <= 0 :
        raise ValueError("모든 입력값은 양수여야합니다.")
        
    return ((final_value / initial_value) ** (1 / years) -1) * 100
