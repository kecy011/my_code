
class FBC:
    parameters = ["pcv", "hb", "rbc", "wbc", "mcv", "mch", "mchc", "platelet", "rdw", "pdw",
                  "neutrophil" "lymphocyte" "monocyte", "eosinophil", "basophil"]

    def __init__(self, age, result):
        assert age <= 7,  f"age{self.age} is not within the age gap!!"
        self.age = age
        self.result = result

    @classmethod
    def display_fbc_parameters(cls):
        for test in cls.parameters:
            print(test)

    def check_age(self):
        while self.age > 7:
            print("age is above the required age limit for the result interpretation"
                  "pls  check the age and input again")
            self.age = int(input("please re_enter patient age:"))
        print("age receive successfully")

    def check_result(self):
        while self.result not in self.parameters:
            print(f"{self.result} is not in {self.parameters} please check properly and re_enter"
                  "patient result.")
            self.result = input("enter patient result:")
        print("result  successfully received and is under review......")


class Differential(FBC):

    def __init__(self, age, result, differential_result=None):
        super().__init__(age, result)
        if differential_result is None:
            differential_result = []
        self.differential_result = differential_result
        print("please enter differential result in order of neutrophil, lymphocyte, monocyte, eosinophil, basophil")

    def neutrophil(self):
        if self.differential_result[0] in range(10, 25):
            print("neutropenia: neutrophil count i low due to sever infection or bone marrow functionality."
                  "please kindly see your doctor or possible treatment or medical advice.")
        elif self.differential_result[0] in range(26, 61):
            print("neutrophil count is okay within the required reference range.")
        elif self.differential_result[0] in range(61, 71):
            print("neutrophilia: patient neutrophil is high due to sepsis (a blood infection ) or bacteria infection"
                  "please kindly see your medical doctor for treatment and medical advice or a trained pharmacy "
                  "for an antibiotic prescription.")
        elif self.differential_result[0] in range(71, 95):
            print("sever neutrophilia: patient neutrophil is very high due to very sever bacteria infection and needs"
                  "urgent medical attention. strongly advice to see a medical practitioner s soon as possible.")
        else:
            print("invalid input for neutrophil count for patient with age group 0-7days old.")

    def get_lymphocyte(self):
        print("please enter lymphocyte result in percentage.")
        if self.differential_result[1] in range(4, 20):
            print("lymphopenia: patient lymphocyte is low due to elevated neutrophil count or a viral infection."
                  "i advice you see a medical practitioner for further test, treatment and medical advice.")
        elif self.differential_result[1] in range(20, 36):
            print("lymphocyte count is okay and within the reference  range.")
        elif self.differential_result[1] in range(36, 61):
            print("lymphocytosis: patient lymphocyte is high due to an a viral infection or bone marrow functionality."
                  "i advice you see your medical doctor for treatment and medical advice.")
        elif self.differential_result[1] in range(61, 91):
            print("sever lymphocytosis: patient lymphocyte is extremely high due to a viral infection "
                  "bone marrow functionality. please see your doctor for urgent medical attention.")
        else:
            print("invalid test input for lymphocyte count of the age group.")

    def get_monocyte(self):
        if self.differential_result[2] in range(1, 6):
            print("monocytopenia: patient monocyte is low due to infection, malaria, or radiation exposure to the "
                  "bone marrow. ")
        elif self.differential_result[2] in range(6, 19):
            print("patient monocyte is normal within the required reference range.")
        elif self.differential_result[2] in range(19, 31):
            print("monocytosis: patient monocyte is high  due to an infection or malaria "
                  "please see your doctor for medical treatment and advice.")
        elif self.differential_result[2] in range(31, 41):
            print("sever monocytosis: patient monocyte is extremely high  to sever infection or bone marrow function."
                  "please see your doctor as soon as possible for urgent medical attention and treatment.")
        else:
            print("invalid input for monocyte result\n result cant be interpreted .out of range!!!!")

    def get_eosinophil(self):
        if self.differential_result[3] in range(0, 3):
            print("patient eosinophil is normal and within the required reference range.")
        elif self.differential_result[3] in range(3, 8):
            print("eosinophilia: patient eosinophil is slightly high above the reference range due to parasitic "
                  "infection, please see your doctor for further test and medical advice")
            print("other suggested test include: stool mcs and urine mcs. ")
        elif self.differential_result[3] in range(8, 15):
            print("sever eosinophilia: patient eosinophil is very high possibly due to sever parasitic infection"
                  "advice to do stool and urine mcs test or see your doctor for treatment and medical advice.")
        else:
            print("invalid input for eosinophil result\n result cant be interpreted .out of range!!!!")

    def get_basophil(self):
        if self.differential_result[4] in range(0, 3):
            print("patient basophil is normal, within the reference range.")
        elif self.differential_result[4] in range(3, 6):
            print("basophilia: patient basophil is high due to possible inflammatory conditions"
                  "please see your doctor for treatment and medical advice")
        else:
            print("invalid input for basophil result\n result cant be interpreted .out of range!!!!")

    @staticmethod
    def get_wbc(wbc):
        print("please enter your wbc result in ul")
        if wbc in range(1-9):
            print("leucocytopenia: patient white blood cell is low ... the immune system is weak due to infection "
                  "advice to see your doctor for medical advice and further test. ")
        elif wbc in range(9, 36):
            print("patient white blood cell is normal and ia within the required reference range.")
        elif wbc in range(36, 56):
            print("leukocytosis: patient wbc is high due to sepsis caused by bacteria infection in the blood."
                  "advice to see your doctor for treatment or see a trained pharmacist for antibiotic prescription")
        elif wbc in range(56, 81):
            print("sever leukocytosis: patient wbc is extremely high due to sever sepsis caused by bacteria infection")
        elif wbc in range(81, 101):
            print("hyper leukocytosis: patient white blood cell is extremely high due to possible sever bacteria "
                  "infection or leukaemia: a blood cancer affecting the white blood cell or whole cll in general"
                  "patient needs urgent medical attention. advice to see your doctor as soon as possible"
                  "for further investigation, treatment and medical advice.")
        else:
            print("invalid input. patient wbc is out of range and cannot be read by yh system, please check properly"
                  "and re_enter wbc.")


class Bloodlevel(FBC):

    def __init__(self, age, request, blood_level_result=None):
        print("anaemia is a medical condition which is due to shorted of red blood cells or the ion carry pigment\n"
              "(haemoglobin there by reducing the oxygen carrying capacity in the blood.this can be life threaten\n"
              "resulting to tissue hyposia(lack of oxygen in cell tissue), brain death leading to ischemic stroke\n"
              "and finally death")

        if blood_level_result is None:
            blood_level_result = []
        print(f"pls enter the result in this order. pcv, hb, rbc")
        super().__init__(age, request)
        self.blood_level_result = blood_level_result

    def get_pcv(self):
        if self.blood_level_result[0] in range(9, 20):
            print("sever anemia:patient blood level is low is due to any of the following reason:"
                  "sever blood loss, iron deficiency, hormonal imbalance(erythropoietin), "
                  "or bone marrow functionality")
        elif self.blood_level_result[0] in range(20, 45):
            print("anemia:patient blood level is low is due to any of the following reason:"
                  " blood loss, iron deficiency, hormonal imbalance(erythropoietin), "
                  "or bone marrow functionality ")
        elif self.blood_level_result[0] in range(45, 68):
            print("patient blood level is okay and within the required reference rage.")
        elif self.blood_level_result[0] in range(68, 76):
            print("polycytemia: patient blood level is high. pls see your doctor for medical "
                  "advice and possible test.advice to do a blood film report.")
        elif self.blood_level_result[0] in range(76, 86):
            print("sever polycytemia: patient blood level is very high and needs urgent medical attention"
                  "please see your doctor as soon as possible for treatment and medical advice"
                  "blood film report is advice.")
        else:
            print("invalid result input for pcv value of patient in age group 0-7days old.")

    def get_hb(self):
        if self.blood_level_result[1] in range(5, 15):
            print("patient haemoglobin is low due to low iron intake or blood loss")
        elif self.blood_level_result[1] in range(15, 24):
            print("patient haemoglobin is fine and within the required reference range.")
        elif self.blood_level_result[1] in range(24, 31):
            print("patient haemoglobin is high due and needs to see a medical doctor for treatment"
                  "and further test investigation. however, blood film is advice.")
        elif self.blood_level_result[1] in range(31, 36):
            print("patient haemoglobin is extremely high!!!!"
                  "patient needs urgent medical attention. please see your doctor as soon as possible.")
        else:
            print("invalid input for haemoglobin result. test input is above the readable range"
                  "please check and re-enter patient hb.")

    def get_rbc(self):
        if self.blood_level_result[1] in range(1, 4):
            print("patient rbc result is low. possible causes are: blood loss. poor diet, haemolytic disease "
                  "due to damage of red blood cells from antibodies as a result of rhesus incompatibility "
                  "between mother and child ")
        elif self.blood_level_result[1] in range(4, 8):
            print("patient rbc result  is fine and within the required reference range.")
        elif self.blood_level_result[1] in range(8, 16):
            print("patient rbc result is high above the normal range. this can be due to the following:"
                  "loss of body fluid, red bone marrow disorder. dangers include: headache, fatigue, blood clot.")
        elif self.blood_level_result[1] in range(16, 26):
            print("sever erythrocytosis:patient rbc is extremely high and needs urgent medical attention."
                  "please see your doctor as urgent as possible for further test, treatment and medical advice.")
        else:
            print("invalid test result for rbc. result is above readable reference renge.")
            while True:
                input("enter rbc result:")


class Rbcidices(FBC):

    def __init__(self, age, request, indices_parameter=None):
        if indices_parameter is None:
            indices_parameter = []
        super() .__init__(age, request)
        self.indices_parameter = indices_parameter
        print("blood indices comprises of the following blood parameters: mcv, mch, mchc"
              "mcv:mean cell corposclar volume. measure the size of the red cell"
              "mch: mean cell haemoglobin. it measures the average concentration of haemoglobin "
              "in one red cell."
              "mchc: mean cell haemoglobin concentration. it measures the the colour of the red cells.")
        print("pls enter rbc indices result in this order: mcv, mch, mchc")

    def get_mcv(self):
        if self.indices_parameter[0] in range(30, 51):
            print("chronic microcytosis: patient mcv is extremely low . suspected iron deficiency anemia"
                  "please see your doctor urgently for treatment and medical advice.")
        elif self.indices_parameter[0] in range(51, 71):
            print("sever microcytosis: patient mcv is very low due to low iron intake and poor diet"
                  "suspected iron deficiency anemia. please see your medical doctor"
                  "for treatment and medical advice.")
        elif self.indices_parameter[0] in range(71, 96):
            pass


p1 = FBC
print(p1.parameters)
print(p1.check_age(4))

