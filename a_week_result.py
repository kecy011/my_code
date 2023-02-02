
class FBC:
    test_parameters = ["pcv", "hb", "rbc", "differential", "rbc_indices", "platelet", "rdw", "pdw"]

    def __init__(self, age: int, request: float):
        self.age = age
        self.request = request

    def get_age(self):
        if self.age > 8:
            print("age is above the required age limit for the result interpretation"
                  "pls check the age and enter again")
        else:
            print("age successfully received and its under processing......"
                  "result for neonate and ref value are different from that of adult"
                  "pls ensure patient is within the required age group. ")

    def get_request(self, investigation):
        if investigation not in self.request:
            print(f"invalid input for request {investigation} is not among test list to be done "
                  f"by a neonate.")
        else:
            print("input successfully received and is under review and being process.")


class Differential(FBC):

    def _init_(self, age, request):
        print("pls enter baby age in days not more than 7 days old.")
        self.age = age
        self.request = request

    def get_age(self):
        if self.age > 7:
            print("age is above the required age limit for the result interpretation"
                  "pls check the age and input again")
        else:
            print("patient is a neonate\n note: the result ref rage and interpretation is for neonate.")

    def get_request(self, investigation):
        if investigation not in self.request:
            print(f"neonate not eligible for{investigation}")
        else:
            print("input successfully received and is under processing......")


class Differential(FBC):
    print("please ensure patient is within the required age group"
          "as this will reflect in the result to avoid miss interpretation of result.")

    def _init_(self, age, request, parameter):
        super().__init__(age, request)
        self.parameter = []

    def get_parameter(self):
        for item in self.parameter:
            if item != str:
                print("invalid test parameter")
            else:
                print(f"welcome,the system will interpret the above test input.pls confirm that{self.parameter} "
                      f"is the required test.")

    @classmethod
    def neutrophil(cls, neutrophil):
        if neutrophil in range(10, 25):
            print("neutropenia: neutrophil count i low due to sever infection or bone marrow functionality."
                  "please kindly see your doctor or possible treatment or medical advice.")
        elif neutrophil in range(26, 61):
            print("neutrophil count is okay within the required reference range.")
        elif neutrophil in range(61, 71):
            print("neutrophilia: patient neutrophil is high due to sepsis (a blood infection ) or bacteria infection"
                  "please kindly see your medical doctor for treatment and medical advice or a trained pharmacy "
                  "for an antibiotic prescription.")
        elif neutrophil in range(71, 95):
            print("sever neutrophilia: patient neutrophil is very high due to very sever bacteria infection and needs"
                  "urgent medical attention. strongly advice to see a medical practitioner s soon as possible.")
        else:
            print("invalid input for neutrophil count for patient with age group 0-7days old.")

    @classmethod
    def get_lymphocyte(cls, lymphocyte):
        print("please enter lymphocyte result in percentage.")
        if lymphocyte in range(4, 20):
            print("lymphopenia: patient lymphocyte is low due to elevated neutrophil count or a viral infection."
                  "i advice you see a medical practitioner for further test, treatment and medical advice.")
        elif lymphocyte in range(20, 36):
            print("lymphocyte count is okay and within the reference  range.")
        elif lymphocyte in range(36, 61):
            print("lymphocytosis: patient lymphocyte is high due to an a viral infection or bone marrow functionality."
                  "i advice you see your medical doctor for treatment and medical advice.")
        elif lymphocyte in range(61, 91):
            print("sever lymphocytosis: patient lymphocyte is extremely high due to a viral infection "
                  "bone marrow functionality. please see your doctor for urgent medical attention.")
        else:
            print("invalid test input for lymphocyte count of the age group.")

    @classmethod
    def monocyte(cls, monocyte):
        if monocyte in range(1, 6):
            print("monocytopenia: patient monocyte is low due to infection, malaria, or radiation exposure to the "
                  "bone marrow. ")
        elif monocyte in range(6, 19):
            print("patient monocyte is normal within the required reference range.")
        elif monocyte in range(19, 31):
            print("monocytosis: patient monocyte is high  due to an infection or malaria "
                  "please see your doctor for medical treatment and advice.")
        elif monocyte in range(31, 41):
            print("sever monocytosis: patient monocyte is extremely high  to sever infection or bone marrow function."
                  "please see your doctor as soon as possible for urgent medical attention and treatment.")
        else:
            print("invalid input for monocyte result\n result cant be interpreted .out of range!!!!")

    @classmethod
    def get_eosinophil(cls, eosinophl):
        if eosinophl in range(0, 3):
            print("patient eosinophil is normal and within the required reference range.")
        elif eosinophl in range(3, 8):
            print("eosinophilia: patient eosinophil is slightly high above the reference range due to parasitic "
                  "infection, please see your doctor for further test and medical advice")
            print("other suggested test include: stool mcs and urine mcs. ")
        elif eosinophl in range(8, 15):
            print("sever eosinophilia: patient eosinophil is very high possibly due to sever parasitic infection"
                  "advice to do stool and urine mcs test or see your doctor for treatment and medical advice.")
        else:
            print("invalid input for eosinophil result\n result cant be interpreted .out of range!!!!")

    @classmethod
    def get_basophil(cls, basophil):
        if basophil in range(0, 3):
            print("patient basophil is normal, within the reference range.")
        elif basophil in range(3, 6):
            print("basophilia: patient basophil is high due to possible inflammatory conditions"
                  "please see your doctor for treatment and medical advice")
        else:
            print("invalid input for basophil result\n result cant be interpreted .out of range!!!!")

    @classmethod
    def get_wbc(cls, wbc):
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


class Anemia(FBC):
    print("anaemia is a medical condition which is due to shorted of red blood cells or the ion carry pigment"
          "(haemoglobin there by reducing the oxygen carrying capacity in the blood.this can be life threaten"
          "resulting to tissue hyposia(lack of oxygen in cell tissue), brain death leading to ischemic stroke"
          "and finally death")
    anemia_parameters = ["pcv", "hb", "rbc"]

    def _init_(self, age, request, blood_level_result):
        print(f"pls enter the result of this test:{self.anemia_parameters}")
        super()._init_(age, request)
        self.blood_level_result = []
        if self.blood_level_result != str:
            print("invalid input for blood level parameter pls check and re_enter.")
            input("please re_enter result. ")
        else:
            print("result successfully receive.")


    def get_pcv(self):
        if self.blood_level_result[0] in range(9, 16):
            print("sever anemia")


