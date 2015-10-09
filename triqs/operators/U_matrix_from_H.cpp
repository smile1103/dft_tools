#include "./U_matrix_from_H.hpp"

namespace triqs { namespace operators {
U_dict_t U_dict_from_H(Op const & h){

 auto U_dict = U_dict_t{};

 for(auto const & term : h){
  double coef = term.coef;
  auto monomial = term.monomial;

  for(auto const & op:monomial){
   std::cout << "indices=" << op.indices.size() << std::endl;
   //op.indices.toto();
  }
  std::cout << std::endl;

  if(monomial.size()==4){
   if(!(monomial[0].dagger && monomial[1].dagger && !monomial[2].dagger && !monomial[3].dagger) || (monomial[0].indices != monomial[3].indices ) ||  (monomial[1].indices != monomial[2].indices )){
    TRIQS_RUNTIME_ERROR << "monomial is not of the form c_dag(i) c_dag(j) c(j) c(i)";
   }
   else{//everything ok
    U_dict.insert({{monomial[0].indices, monomial[1].indices},coef});
    U_dict.insert({{monomial[1].indices, monomial[0].indices},coef});
   }
  }
  else{
   TRIQS_RUNTIME_ERROR << "monomial must have 4 operators";
  }
 }//h

 return U_dict;
}


matrix<double> U_matrix_from_U_dict(U_dict_t const & U_dict, gf_struct_t const & gf_struct){

 int i_tot=0;
 auto keys_map=std::map<Op::indices_t, int>{};
 for(auto const & kv : gf_struct){
   for(auto const & inner_ind : kv.second){
    keys_map.insert({{kv.first, inner_ind},i_tot});  
    i_tot++;
   }
 }

 auto U_matrix = matrix<double>(keys_map.size(),keys_map.size());
 U_matrix()=0.0;

 for(auto const & kv : U_dict){
   U_matrix(keys_map[kv.first.first],keys_map[kv.first.second]) = kv.second;
 }
 return U_matrix;
}

}}
