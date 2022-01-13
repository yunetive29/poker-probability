#include <iostream>
#include <cmath>
#include <deque>
#include <algorithm>
#include <map>
#include <string>
#include <set>
using namespace std;


//функция по вводу пользователем масти карты с защитой от неправильного формата ввода
int suit_input(int i) {
    int ans = 0;
    while (ans == 0) {
        cout << "Enter the suit of the card " << i + 1 << endl << "# - heart" << endl << "* - diamond" << endl << "@ - club" << endl << " & - spade" << endl;
        string m;
        cin >> m;
        if (m == "#") {
            ans = 4;
        }
        else if (m == "@") {
            ans = 3;
        }
        else if (m == "*") {
            ans = 2;
        }
        else if (m == "&") {
            ans = 1;
        }
        else {
            cout << "Incorrect input format.Enter again" << endl;
        }
    }
    return ans;
}


//функция по вводу пользователем номинала карты с защитой от неправильного формата ввода
int nominal_input(int i) {
    int ans = 0;
    while (ans == 0) {
        cout << "Enter the face value of the card " << i + 1 << endl << "A - ace" << endl << "K - king" << endl << "Q - queen" << endl << "J - jack" << endl << "or a number from 2 to 10" << endl;
        string nom;
        cin >> nom;
        transform(nom.begin(), nom.end(), nom.begin(), toupper);
        if (nom == "A") {
            ans = 14;
        }
        else if (nom == "K") {
            ans = 13;
        }
        else if (nom == "Q") {
            ans = 12;
        }
        else if (nom == "J") {
            ans = 11;
        }
        else if (nom == "10") {
            ans = 10;
        }
        else if (nom == "9") {
            ans = 9;
        }
        else if (nom == "8") {
            ans = 8;
        }
        else if (nom == "7") {
            ans = 7;
        }
        else if (nom == "6") {
            ans = 6;
        }
        else if (nom == "5") {
            ans = 5;
        }
        else if (nom == "4") {
            ans = 4;
        }
        else if (nom == "3") {
            ans = 3;
        }
        else if (nom == "2") {
            ans = 2;
        }
        else {
            cout << "Incorrect input format. Enter again" << endl;
        }
    }
    return ans;
}



//функция для вычисления факториала
unsigned int factorial(unsigned int n)
{
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}



//функция для вычисления ц из н по к
int c_iz_n_po_k(unsigned int n, unsigned int k) {
    int ans;
    ans = factorial(n) / (factorial(k) * factorial(n - k));
    return ans;
}



//функция проверки наличия флеш рояля на руке
bool Royal_Flush_check(bool straight_flash, int max_card) {
    bool ans;
    if (straight_flash == true and max_card == 14) {
        ans = true;
    }
    else {
        ans = false;
    }
    return ans;
}


//функция проверки наличия флеш стрита на руке
bool Straight_Flush_check(bool flash, bool straight) {
    bool ans;
    if (flash == true and straight == true) {
        ans = true;
    }
    else {
        ans = false;
    }
    return ans;
}


//функция проверки наличия каре на руке
bool kare_check(int a, int  b) {
    bool ans;  
    if (a == 4 and b < 2) {
        ans = true;
    }
    else {
        ans = false;
    }
    return ans;
}


//функция проверки наличия фул хауса на руке
bool full_house_check(int a, int  b) {
    bool ans;
    if (a == 3 and b == 2 or a == 2 and b == 3) {
        ans = true;
    }
    else {
        ans = false;
    }
    return ans;
}


//функция проверки наличия флеша на руке
bool Flush_check(deque<int>checker) {
    bool ans = true;
    for (int i = 1; i < 5; i++) {
        if (checker[i] != checker[i - 1]) {
            ans = false;
        }
    }
    return ans;
}


//функция проверки наличия стрита на руке
bool Straight_check(deque<int>checker) {
    bool ans = true;
    int j = 1;
    if (checker[0] == 14 and checker[1] == 5) {
        j++;
    }
    for (int i = j; i < 5; i++) {
        if (checker[i] != checker[i - 1] - 1) {
            ans = false;
        }
    }
    return ans;
}


//функция проверки наличия сета на руке
bool set_check(int a, int  b) {
    bool ans;
    if (a == 3 and b < 2) {
        ans = true;
    }
    else {
        ans = false;
    }
    return ans;
}


//функция проверки наличия двух пар на руке
bool two_pairs_check(int a, int  b) {
    bool ans;
    if (a == 2 and b == 2) {
        ans = true;
    }
    else {
        ans = false;
    }
    return ans;
}


//функция проверки наличия пары на руке
bool pair_check(int a, int  b) {
    bool ans;
    if (a == 2 and b < 2) {
        ans = true;
    }
    else {
        ans = false;
    }
    return ans;
}








//ищем флеш рояли,которые не могут быть составлены исходя из наших карт на руке
int Flush_Royal_ruined(deque<int>noms, deque<int>suits) {
    int sum = 0;
    set<int>checker;
    for (int i = 0; i < 5; i++) {
        if (noms[i] > 9) {
            checker.insert(suits[i]);
        }
    }
    sum = checker.size();
    return sum;
}



//ищем флеш стриты,которые не могут быть составлены исходя из наших карт на руке
int Flush_straight_ruined(bool a, deque<int>noms, deque<int>suits) {
    if (noms[0] == 14) {
        noms.push_back(1);
        suits.push_back(suits[0]);
    }
    int sum = 0;
    if (a == true) {
        sum += max(15 - 5 - noms[0], 0);
        sum += (15 - noms[0]) * 3;
    }
    else {
        while (noms.size() > 0) {
            deque<int>checker(0);
            for (int i = 0; i < noms.size(); i++) {
                int temp = suits[0];
                if (suits[i] == temp) {
                    checker.push_back(noms[i]);
                    noms.erase(noms.begin() + i--);
                    suits.erase(suits.begin() + i--);
                }
                for (int i = 0; i < checker.size();i++) {
                    int maxi = checker[i];
                    int mini = checker[i];
                    checker.push_back(15);
                    while (checker[i] - checker[i + 1] < 5) {
                        mini = checker[i + 1];
                    }
                    sum = min(15 - maxi, 5) + (maxi - mini) + min(mini, 5); 
                }
            }
        }
    }
    return 0;
}



//ищем каре,которые не могут быть составлены исходя из наших карт на руке
int kare_ruined(bool a, deque<int>noms) {
    int sum = 0;
    set<int>checker;
    for (int i = 0; i < 5; i++) {
        checker.insert(noms[i]);
    }
    sum = checker.size();
    return sum;
}



int full_house_ruined(bool a, deque<int>noms, deque<int>suits) {
    return 0;
}



//ищем флеши,которые не могут быть составлены исходя из наших карт на руке
int flush_ruined(bool a, deque<int>noms, deque<int>suits) {
    int ans = 0;
    if (a == false) { //в случае, когда у нас на руках нет флеша
        deque<int>dif_suit(4);
        for (int i = 0; i < 4; i++) {
            dif_suit[i] = 0;
        }
        for (int i = 0; i < 5; i++) {
            switch (noms[i]) {
            case 1:
                dif_suit[0]++;
            case 2:
                dif_suit[1]++;
            case 3:
                dif_suit[2]++;
            case 4:
                dif_suit[3]++;
            }
        }
        for (int i = 0; i < 4; i++) {
             ans += c_iz_n_po_k(13 - dif_suit[i], 5);
        }
    }
    else { //в случае, когда на руках есть флеш (учитываются только флеши старше нашего)

    }
    return ans;
}



int straight_ruined(bool a, deque<int>noms, deque<int>suits) {
    return 0;
}



int set_ruind(bool a, deque<int>noms, deque<int>suits) {
    return 0;
}



int two_pairs_ruined(bool a, deque<int>noms, deque<int>suits) {
    return 0;
}



int pair_ruined(bool a, deque<int>noms, deque<int>suits, int first_vid) {
    int sum = 0;
    if (a == false) {
        for (int i = 0; i < 5; i++) {
            sum += 3;
        }
    }
    return sum;
}




int main()
{
    //Создаем два массива. Первый со старшинствами наших карт и массив с мастями наших карт, соответсвующий ему.
    deque<int>nominalo(5);
    deque<int>suit(5);
    // Пользователь заполняет наши массивы с проверкой на корректность входных данных и повторение карт.
    for (int i = 0; i < 5; i++) {
        bool flag;
        do {
            flag = false;
            nominalo[i] = nominal_input(i);
            suit[i] = suit_input(i);
            for (int j = 0; j < i; j++) {
                if (nominalo[i] == nominalo[j] and suit[i] == suit[j]) {
                    flag = true;
                    cout << "This card is already present. Enter another" << endl;
                }
            }
        } while (flag == true);
        system("cls");
    
    }
    // Сортируем массив с номиналами карт по возрастанию для удобной дальнейшей работы с рукой игрока (тк порядок карт нам не важен, мы можем сделать это). Так же при изменение порядка карт, меняем и соответсвующие масти этих карт.
    for (int i = 0; i < 5; i++) {
        int tmpnominalo,tmpmast;
        for (int j = 0; j < 5 - i - 1; j++) {
            if (nominalo[j] < nominalo[j+1]) {
                tmpnominalo = nominalo[j];
                nominalo[j] = nominalo[j + 1];
                nominalo[j + 1] = tmpnominalo;
                tmpmast = suit[j];
                suit[j] = suit[j + 1];
                suit[j + 1] = tmpmast;
            }
        }
    }
    // Фокус, чтобы не вылезти за границу массива
    nominalo.push_back(-999999);

    int max_card = nominalo[0];
    //находим все повторы карт по их номиналу
    int first_vid = -1, first_kolvo = 0, second_vid = -1, second_kolvo = 0;
    for (int i = 0; i < 4; ++i) {
        while (nominalo[i] == nominalo[i + 1] and i<4) {
            if (first_vid == -1) {
                first_vid = nominalo[i];
                first_kolvo = 2;
            }
            else if (nominalo[i] == first_vid) {
                first_kolvo++;
            }
            else if (nominalo[i] != first_vid and second_vid == -1) {
                second_vid = nominalo[i];
                second_kolvo = 2;
            }
            else if (second_vid == nominalo[i]) {
                second_kolvo++;
            }
            i++;
        }
    }


    nominalo.pop_back();


    //наименования всех комбинаций
    deque<string>comb_name(10);
    comb_name[0] = "Royal Flush";
    comb_name[1] = "Straight Flush";
    comb_name[2] = "Kare";
    comb_name[3] = "Full House";
    comb_name[4] = "Flush";
    comb_name[5] = "Straight";
    comb_name[6] = "Set";
    comb_name[7] = "Two Pairs";
    comb_name[8] = "Pair";
    comb_name[9] = "The Highest Card";


    //Проверка наличия каждой из комбинация у нас на руках
    deque<bool>combinations_avaliability(10);
    combinations_avaliability[2] = kare_check(first_kolvo, second_kolvo);
    combinations_avaliability[3] = full_house_check(first_kolvo,second_kolvo);
    combinations_avaliability[4] = Flush_check(suit);
    combinations_avaliability[5] = Straight_check(nominalo);
    combinations_avaliability[1] = Straight_Flush_check(combinations_avaliability[4], combinations_avaliability[5]);
    combinations_avaliability[0] = Royal_Flush_check(combinations_avaliability[1], max_card);
    combinations_avaliability[6] = set_check(first_kolvo, second_kolvo);
    combinations_avaliability[7] = two_pairs_check(first_kolvo, second_kolvo);
    combinations_avaliability[8] = pair_check(first_kolvo, second_kolvo);
    combinations_avaliability[9] = true;


    deque<int>ruined_combintions(10);
    

    //нахождение индекса наивысшей комбинации
    int hcomb_index = 0;
    while (combinations_avaliability[hcomb_index] != true) {
        ++hcomb_index;
    }


    //Нахождение кикера
    int kicker;
    if (hcomb_index >= 6 and hcomb_index <= 8 or hcomb_index == 2) {
        for (int i = 0; i < 5; i++) {
            if (nominalo[i] != first_vid and nominalo[i] != second_vid) {
                kicker = nominalo[i];
                break;
            }
        }
    }


    //вероятность выпадения каждой из комбинация среди 5 карт из колоды в соответсвии с их наименованиями по индексу
    deque<double>comb_probability(10);
    comb_probability[0] = 0.0001539077;
    comb_probability[1] = 0.0013851695;    
    comb_probability[2] = 0.0240096038;
    comb_probability[3] = 0.144057623;
    comb_probability[4] = 0.1965401545;
    comb_probability[5] = 0.3924646782;
    comb_probability[6] = 2.1128451381;
    comb_probability[7] = 4.7539015606;
    comb_probability[8] = 42.2569027611;
    comb_probability[9] = 50.1177394035;

    double sum = 0.0;
    double win_prob;

    //считаем вероятноть ничьи или поражения
    for (int i = hcomb_index - 1; i >= 0; --i) {
        cout << comb_name[i] << endl;
        sum = sum + comb_probability[i];
    }
    if (hcomb_index == 0) {
        sum += (comb_probability[hcomb_index] * 3) / 4;
    }
    else if (hcomb_index == 1) {
        sum += (comb_probability[hcomb_index] * (13 - max_card + 1)) / 10;
        sum += (comb_probability[hcomb_index] / 10) * 3 / 4;
    }
    else if (hcomb_index == 2) {
        sum += (comb_probability[hcomb_index] * (13 - first_vid + 1)) / 13;
    }
    else if (hcomb_index == 3) {
        sum += (comb_probability[hcomb_index] * (13 - first_vid + 1)) / 13;
    }
    else if (hcomb_index == 4) {
        for (int i = 0; i < 5; i++) {
            sum += ((comb_probability[hcomb_index] / (pow(13, i)) * (13 - nominalo[i] + 1))) / 13;
        }
        sum += comb_probability[hcomb_index];
    }
    else if (hcomb_index == 5) {
        sum += (comb_probability[hcomb_index] * (13 - max_card + 1)) / 10;
        sum += ((comb_probability[hcomb_index] / 10) * 3) / 4;
    }
    else if (hcomb_index == 6) {
        sum += (comb_probability[hcomb_index] * (13 - first_vid + 1)) / 13;

    }
    else if (hcomb_index == 7) { 
        sum += (comb_probability[hcomb_index] * (11 * 10 + 1) * (13 - kicker + 1 + 1)) / (13 * 13 * 12);
        sum += (comb_probability[hcomb_index] * ((13*12 - (11 * 10 + 1)) / 2) * (13 - first_vid + 1)) / (13 * 13 * 12);
        sum += (comb_probability[hcomb_index] * ((13 * 12 - (11 * 10 + 1)) / 2) * (13 - second_vid + 1)) / (13 * 13 * 12);
    }
    else if (hcomb_index == 8) {
        sum += (comb_probability[hcomb_index] * (13 - first_vid + 1)) / 13;
        sum += ((comb_probability[hcomb_index] / 13) * (13 - kicker + 1 + 1)) / 13;
    }
    else if (hcomb_index == 9) {
        sum += (comb_probability[hcomb_index] * (13 - max_card + 1)) / 13;
        sum += ((comb_probability[hcomb_index]) * 3) / 4;
    }
    

    //итоговая вероятность
    win_prob = 100 - sum;


    //вывод данных
    cout << endl << "Your combination:" << endl << endl << comb_name[hcomb_index] << endl;
    cout << endl;
    cout << "Your win probability:" << endl << endl << win_prob << "%" << endl;
    cout << endl;
    system("pause");

    return 0;
}
